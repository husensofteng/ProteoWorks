# Search Enigne Evaluation - ongoing
The purpose of this workshop is to find an algorithm that can identify a larger number of hits in the deep proteomics datasets generated at our lab. 

- Details about each tool, including documentation and specifications, should be reported in s correponding directory of the tool.

- Only breif results to inform about the current status of run and final results should be reported here.

Guidelines for running the tools
---
In order to obtain comparable results across the tools, we have specified the following parameters and datasets to be used for each whenever possible. Otherwise, state clearly in the tool's documentation if another variant is used.

### Parameters

### Datasets
- mzML files

- protein sequence databases


## Open-pFind (open database search)
windows-based and requires 

finished running (49mins) on 2 cores

accepts mzML and raw files, no decoy is needed.

## MSFragger (open database search): Taner, Mattias V, Tanvir
Java-based

Finished running, output is: a psm table per fraction,  peptide_xml per fraction 

to do:

- Combine the tables and convert to pin format for percolator.
- Get MS quants for each PSM

## TagGraph (de novo + database search): Husen, Ioannis, Rui, Yan
ran it on their sample input data and it works but needs to be run on our data

to do:

- try PEAKS or some other denovo algorithm and run it on the mzML files to generate a peptide csv file 
- run the docker image on the data and get output

## COSS (spectral library search):  Matthias, Mohammad
Java-based

problem with generating spectra libs, used an available one but failed and gave some exception. 

The tool seems unmature so dismiss for now.

## Comet*: Jorrit, David
mzML
12,700 psms (not sure) using FDR 1% (percolator)

# Others (optional):
## MS-Amanda*: Husen, Ioannis, Rui
not tried yet

## X!Tandem*: (Jorrit, David)
not tied yet

## MaxQuant: Maan, Mohammad
not tied yet

## MS-GF+ (Jorrit)
linux-based, mzML, accepts decoy

output: 17,878 psms (ENSEMBL data, human_ecoli)

to do:

- MS quant extraction

## Morpheus (Matthias&Mohammad)
windows-based (ran with mono), decoy (optional), accepts mzML

running, ~10min for 1 fraction

## SEQUEST
not tried yet

## Mascot
not tried yet
