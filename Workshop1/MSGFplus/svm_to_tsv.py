import os, sys
from app.readers import pycolator, xml, tsv, mzidplus

def svm_to_tsv(mzid_file, mzid_tsv_file, filtprot_xml_infile, outfile = ".tsv"):
    
    if os.path.isfile(outfile):
        return outfile
    
    ns = xml.get_namespace_from_top(filtprot_xml_infile, None)
    psms = {p.attrib['{%s}psm_id' % ns['xmlns']]: p for p in pycolator.generate_psms(filtprot_xml_infile, ns)}
    decoys = {True: 0, False: 0}
    for psm in sorted([(pid, float(p.find('{%s}svm_score' % ns['xmlns']).text), p) for pid, p in psms.items()], reverse=True, key=lambda x:x[1]):
        pdecoy = psm[2].attrib['{%s}decoy' % ns['xmlns']] == 'true'
        decoys[pdecoy] += 1
        try:
            psms[psm[0]] = {'decoy': pdecoy, 'svm': psm[1], 'qval': decoys[True]/decoys[False]}  # T-TDC
        except ZeroDivisionError:
            psms[psm[0]] = {'decoy': pdecoy, 'svm': psm[1], 'qval': 1.0}  # T-TDC
    decoys = {'true': 0, 'false': 0}
    for svm, pep in sorted([(float(x.find('{%s}svm_score' % ns['xmlns']).text), x) for x in pycolator.generate_peptides(filtprot_xml_infile, ns)], reverse=True, key=lambda x:x[0]):
        decoys[pep.attrib['{%s}decoy' % ns['xmlns']]] += 1
        try:
            [psms[pid.text].update({'pepqval': decoys['true']/decoys['false']}) for pid in pep.find('{%s}psm_ids' % ns['xmlns'])]
        except ZeroDivisionError:
            [psms[pid.text].update({'pepqval': 1.0}) for pid in pep.find('{%s}psm_ids' % ns['xmlns'])]
    oldheader = tsv.get_tsv_header(mzid_tsv_file[0])
    header = oldheader + ['percolator svm-score', 'PSM q-value', 'peptide q-value']
    with open(outfile, 'w') as fp:
        fp.write('\t'.join(header))
        for fnix, mzidfn in enumerate(mzid_file):
            mzns = mzidplus.get_mzid_namespace(mzidfn)
            siis = (sii for sir in mzidplus.mzid_spec_result_generator(mzidfn, mzns) for sii in sir.findall('{%s}SpectrumIdentificationItem' % mzns['xmlns']))
            for specidi, psm in zip(siis, tsv.generate_tsv_psms(mzid_tsv_file[fnix], oldheader)):
                scan, rank = specidi.attrib['id'].replace('SII_', '').split('_')
                outpsm = {k: v for k,v in psm.items()}
                spfile = os.path.splitext(psm['#SpecFile'])[0]
                try:
                    percopsm = psms['{fn}_SII_{sc}_{rk}_{sc}_{ch}_{rk}'.format(fn=spfile, sc=scan, rk=rank, ch=psm['Charge'])]
                except KeyError:
                    continue
                if percopsm['decoy']:
                    continue
                fp.write('\n')
                outpsm.update({'percolator svm-score': percopsm['svm'], 'PSM q-value': percopsm['qval'], 'peptide q-value': percopsm['pepqval']})
                fp.write('\t'.join([str(outpsm[k]) for k in header]))
        fp.write('\n')
    return outfile
mzid_files = ['GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr07.mzid', 'GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr08.mzid', 'GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr09.mzid']
mzid_tsv_files = ['GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr07.mzid.tsv', 'GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr08.mzid.tsv', 'GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr09.mzid.tsv']

svm_tsv_file = svm_to_tsv(mzid_files, mzid_tsv_files, filtprot_xml_infile=sys.argv[1], outfile = sys.argv[2])


def create_psm_table(svm_tsv_file, mzml_sqlitedb, psmtable_outfile):
    os.system("msspsmtable conffilt -i {svm_tsv_file} -o {svm_tsv_file}_filtpsm \
                --confidence-better lower --confidence-lvl 0.01 --confcolpattern 'PSM q-value'".format(svm_tsv_file=svm_tsv_file))

    os.system("msspsmtable conffilt -i {svm_tsv_file}_filtpsm -o {svm_tsv_file}_filtpsm_filtpep \
                --confidence-better lower --confidence-lvl 0.01 --confcolpattern 'peptide q-value'".format(
                    svm_tsv_file = svm_tsv_file))
    os.system("msslookup psms -i {svm_tsv_file}_filtpsm_filtpep --dbfile {mzml_sqlitedb}".format(svm_tsv_file=svm_tsv_file,
                                                                                                      mzml_sqlitedb=mzml_sqlitedb))

    os.system("msspsmtable specdata -i {svm_tsv_file}_filtpsm_filtpep --dbfile {mzml_sqlitedb} -o {svm_tsv_file}_filtpsm_filtpep_prepsms.txt".format(svm_tsv_file = svm_tsv_file, mzml_sqlitedb = mzml_sqlitedb))

    os.system("msspsmtable quant -i {svm_tsv_file}_filtpsm_filtpep_prepsms.txt -o {psmtable_outfile} --dbfile {mzml_sqlitedb} --isobaric".format(svm_tsv_file = svm_tsv_file, mzml_sqlitedb = mzml_sqlitedb, psmtable_outfile=psmtable_outfile))

    os.system("sed 's/\#SpecFile/SpectraFile/' -i {psmtable_outfile}".format(psmtable_outfile = psmtable_outfile))


psm_table_file = create_psm_table(svm_tsv_file, mzml_sqlitedb='mslookup_db.sqlite', psmtable_outfile="sig_psms.tsv")
