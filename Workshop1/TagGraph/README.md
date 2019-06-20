## Steps to run TagGrap

1. Download the Docker image for TagGraph
-------------
https://sourceforge.net/projects/taggraph/files/Current%20Release/DockerContainer/linux/CentosDockerTG.1.7.1.tar.gz/download

Change the downloaded file name and extract
---
`mv download taggraph.tar.gz`

`tar -xzvf taggraph.tar.gz`

Configure the input params file in
-----
copy this file `sampleInputFiles/TG/A375mzML.ini` into `path_to_confi_file.ini`

Run a denovo seq tool
----
A separate tool (pepNovo, etc) should be run on each mzML file to get peptide sequences and give that as input to TagGraph

Index the protein databases using FMindex from TagGraph
----
```sudo docker run --name taggraph --rm -v /:/virenv -i inf/taggraph:v1 python /opt/bio/tools/taggraph/TagGraph.1.7.1/scripts/Build_FMIndex_new.py -f /virenv/path_to_fasta_files/Human_Ecoli_target.fasta  -o /virenv/path_to_fasta_files/Human_Ecoli_target | tee mzml.log```


Run the TagGraph
-----
```sudo docker run --name taggraph --rm -v `pwd`:`pwd` -w`pwd` -i -t inf/taggraph:v1 python /opt/bio/tools/taggraph/TagGraph.1.7.1/runTG.py path_to_confi_file.ini | tee mzml.log```


