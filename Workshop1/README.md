# Search Enigne Evaluation


Status or Results from different tools
------

## Open-pFind (open database search)
windows-based and requires 
running (22mins on 3 fractions and still runs) on 2 cores

## MSFragger (open database search): Taner, Mattias V, Tanvir
Java-based

Finished running, output is: a psm table per fraction,  peptide_xml per fraction 

to do:
----
- Combine the tables and convert to pin format for percolator.
- Get MS quants for each PSM

## TagGraph (de novo + database search): Husen, Ioannis, Rui, Yan
ran it on their sample input data and it works but needs to be run on our data

to do:
-----
- try PEAKS or some other denovo algorithm and run it on the mzML files to generate a peptide csv file 
- run the docker image on the data and get output

## COSS (spectral library search):  Matthias, Mohammad
Java-based

problem with generating spectra libs, used an available one but failed and gave some exception. The tool seems unmature so dismiss for now.

## Comet*: Jorrit, David
## Others (optional):
## MS-Amanda*: Husen, Ioannis, Rui
## X!Tandem*: (Jorrit, David)
## MaxQuant: Maan, Mohammad
## MS-GF+ (Jorrit), 
## Morpheus (Matthias&Mohammad), 
## SEQUEST
