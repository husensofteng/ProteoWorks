# MSGF+ results

Commands to run
---
Run the cmd.sh command

it does:
- generate concensusXML for each mzML file
- run each mzML file against the database fasta file, generates mzid file
- convert mzid files into tsv
- convert mzid files into percolator tsv input
- create an sqlitedb file from mzML files
- get quants from the consensusXML files and the spectra files
- run (svm_to_tsv) that calculates FDR for each peptide and filters the results, generates final psm table

Results
----
Run 8-Jul-2019-Husen: 33,106 PSMs and 17,101 peptides



