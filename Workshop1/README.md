# Search Enigne Evaluation - ongoing
The purpose of this workshop is to find an algorithm that can identify a larger number of hits in the deep proteomics datasets generated at our lab. See related [slides](https://docs.google.com/presentation/d/1TGD3SQ75VlNbgXM7J1cSvQtAXrDQMzNCU4HXLqAFM3Y/edit?usp=sharing). 

- Details about each tool, including documentation and specifications, should be reported in s correponding directory of the tool.

- Only breif results to inform about the current status of run and final results should be reported here.


Guidelines for running the tools
---
In order to obtain comparable results across the tools, we have specified the following parameters and datasets to be used for each whenever possible. Otherwise, state clearly in the tool's documentation if another variant is used.

### Parameters
1. peptides:
  - Tryptic only cut (P or K, except RP and KP)
  - One missed cleavage is allowd
  - No semi-tryptic peptides
2. PTMs
  - OX (M) var (max 2 per peptide): 15.994915 (avg 15.9994)
  - CARRAM100Methyl (c) fix: 57.021464 (avg 57.0513)
  - TMT6Plex (N, K) fix: 229.162932 (avg 229.2634)
3. Algorithm
  - Tolerance: MS1: 10ppm; MS2: 0.02Da
  - Recursor sie: max: 5000 or 6000 Da and min: 700
  - Charge states: 2-6
4. [Comparison criteria](https://docs.google.com/presentation/d/1TGD3SQ75VlNbgXM7J1cSvQtAXrDQMzNCU4HXLqAFM3Y/edit#slide=id.g59a9f429fd_0_21): 

### Datasets
1. MS dataset - Human_Ecoli (mzML and raw files are available)
  - fractions 7, 8 and 9 from The TMT set (partial, for testing purposes)
  - All 40 fractions from the TMT set (full, for final results, ask for request)
  
2. Protein databases (located uner the datasets/ directory)
  - Human and E.coli protein databases (human_ecoli_target.fa, use the uniprot version)
  - Decoy for the Human and Ecoli databases (human_ecoli_decoy.fa)
  - Human, E.coli and Pfu protein databases (human_ecoli_pfu_target.fa) for 
  - Decoy for the Human, Ecoli and Pfu databases (human_ecoli_pfu_decoy.fa)

### Scripts for post-processing the search output files, if needed (to be done).
  - output to percolator input
  - get MS quants for the identified PSMs
  - collecting the comparison params

Recent Search Algorithms
----

### Open-pFind (open database search): Rui, Maan, Yanbo 
windows-based, 64-bit only, require activation to run

finished running in : 49mins  (using 2 cores)

accepts as input: mzML, raw, MGF or WIFF files, no decoy database is needed.

Detailed parameters and results are found in pFind3 directory.

### MSFragger (open database search): Taner, Mattias V, Tanvir
Java-based

Finished running, output is: a psm table per fraction,  peptide_xml per fraction 

to do:

- Combine the tables and convert to pin format for percolator.
- Get MS quants for each PSM

### TagGraph (de novo + database search): Husen, Ioannis, Rui, Yan
ran it on their sample input data and it works but needs to be run on our data

to do:

- try PEAKS or some other denovo algorithm and run it on the mzML files to generate a peptide csv file 
- run the docker image on the data and get output

### COSS (spectral library search):  Matthias, Mohammad
Java-based

problem with generating spectra libs, used an available one but failed and gave some exception. 

The tool seems unmature so dismiss for now.

### Comet*: Jorrit, David
mzML
12,700 psms (not sure) using FDR 1% (percolator)




Other Search Algorithms (Optional)
----

### MS-Amanda*: Husen, Ioannis, Rui
PSMs identified, not analyzed yet

### X!Tandem*: (Jorrit, David)
not tied yet

### MaxQuant: Maan, Mohammad
not tied yet

### MS-GF+ (Jorrit)
linux-based, mzML, accepts decoy

output: 17,878 psms (ENSEMBL data, human_ecoli)

to do:

- MS quant extraction

### Morpheus (Matthias&Mohammad)
windows-based (ran with mono), decoy (optional), accepts mzML

running, ~10min for 1 fraction

### SEQUEST (Rui)
PSMs identified, not analyzed yet

### Mascot
not tried yet

### Byonic (Rui)
PSMs identified, not analyzed yet
