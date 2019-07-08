#python ~/pipelines/ProteoGenomics/IdentifyCanonicalPeptides.py --mzmls_metafile mzML_files --mods_file ~/pipelines/ProteoGenomics/Mods.txt --canonical_pep_db /Z/husen/pipelines/ProteoWorks/Workshop1/datasets/Uniprot_sp-Human_refp-EcoliK12_20190620_targetdecoy.fasta --output_dir Uniprot_Human_Ecoli --verbose --plex_type tmt6plex

mods_file='/Z/husen/pipelines/ProteoWorks/Workshop1/MSGFplus_fr_manual_tmt10/Mods.txt'
db_file='/Z/husen/pipelines/ProteoWorks/Workshop1/datasets/Uniprot_sp-Human_refp-EcoliK12_20190620_targetdecoy.fasta'
output_dir='/Z/husen/pipelines/ProteoWorks/Workshop1/MSGFplus_fr_manual_tmt10/'
set_name="set1"
mzmls_path="/Z/husen/pipelines/ProteoWorks/Workshop1/MSGFplus_fr_manual_tmt10/mzMLs/*.mzML"
mzmls=`ls $mzmls_path`
echo $mzmls


for mzml in $mzmls
do
	mzml_name=`echo $mzml | python -c "import sys; print([''.join(s.strip().split('/')[-1].split('.')[0:-1]) for s in sys.stdin][0])"`
	if [ ! -f $output_dir$mzml_name".consensusXML" ]; then
		echo "Generating results for: "$output_dir$mzml_name".consensusXML"
		#get consensusXML_file for feach mzML file
		docker run -v /:/virenv biocontainers/openms IsobaricAnalyzer -type tmt10plex -in /virenv/$mzml -out /virenv/$output_dir$mzml_name".consensusXML" -extraction:select_activation hcd -extraction:reporter_mass_shift 0.0013 -extraction:min_precursor_intensity 1.0 -extraction:keep_unannotated_precursor true -quantification:isotope_correction true
	fi
done

for mzml in $mzmls
do
	mzml_name=`echo $mzml | python -c "import sys; print([''.join(s.strip().split('/')[-1].split('.')[0:-1]) for s in sys.stdin][0])"`
	if [ ! -f $mzml_name".mzid" ]; then
		echo "Generating results for: "$mzml
		#run msgf_plus on each mzML file
		docker run -v /:/virenv quay.io/biocontainers/msgf_plus:2016.10.26--py27_1 msgf_plus -Xmx30000M -d /virenv/$db_file -s /virenv/$mzml -o /virenv/$output_dir$mzml_name".mzid" -thread 16 -mod /virenv/$mods_file -tda 0 -t 10.0ppm -ti -1,2 -m 0 -inst 3 -e 1 -protocol 0 -ntt 2 -minLength 7 -maxLength 40 -minCharge 2 -maxCharge 6 -n 1 -addFeatures 1

		docker run -v /:/virenv quay.io/biocontainers/msgf_plus:2016.10.26--py27_1 msgf_plus -Xmx30000M edu.ucsd.msjava.ui.MzIDToTsv -i /virenv/$output_dir$mzml_name".mzid" -o /virenv/$output_dir$mzml_name".mzid.tsv"
	fi
done

#run percolator on the combined mzid files
echo `ls $output_dir/*.mzid` | awk '{gsub(" ", "\n"); print}' > metafile
msgf2pin -o percoin.tsv -e trypsin -P "decoy_" metafile
percolator -j percoin.tsv -X perco.xml -N 500000 --decoy-xml-output -y

#create sqlitedb from the mzML spectra files
n=`ls $mzmls_path | wc -l`
set_names=`python -c "x=[]; print(' '.join(['$set_name' for i in range(0,$n)]))"`
msslookup spectra -i $mzmls --setnames $set_names

#add quants to the tables in the sqlitedb file
xmls=$output_dir"*.consensusXML"
cons_xmls=`ls $xmls`
echo $cons_xmls
msslookup isoquant --dbfile mslookup_db.sqlite -i $cons_xmls --spectra $mzmls

#calcualte FDR based on the decoy results and filter psms based on the peptide-level fdr and return sig_psm_table.tsv
python svm_to_tsv.py perco.xml perco.tsv
