# Morpheus
>for high-resolution tandem mass spectra

Group members: Mohammad and Matthias

[Paper](https://pubs.acs.org/doi/10.1021/pr301024c)
[Command line arguments](http://cwenger.github.io/Morpheus/args.html)


## About the search engine
- for high-resolution MS/MS
- very simple scoring function (fast?)

## Run
1. Download `fasta` databases.
2. Get [Morpheus](http://cwenger.github.io/Morpheus/) and [mono](https://www.mono-project.com/download/stable/) (as we are running on MacOS).
3. Run:
  
  ```
  mono morpheus_mzml_mono_cl.exe -d "../../../../data/GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr07.mzML,../../../../data/GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr08.mzML,../../../../data/GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr09.mzML" -minprecz 2 -maxprecz 6 -db "../../../../db/Human_Ecoli_target.fa" -ad true -p "trypsin" -mmc 1 -fm "carbamidomethylation of C;TMT sixplex/tenplex on peptide N-terminus;TMT sixplex/tenplex on K" -vm "oxidation of M" -precmtv 10.0 -precmtu "ppm" -minpmo 0 -maxpmo 0 -prodmtv 0.02 -prodmtu "Da" -mt 4 -o "../results"
  ```
  CAVE: Only relative paths work!
5. Among others, got this error:
  
  ```
  System.AggregateException: One or more errors occurred. (Index was outside the bounds of the array.) (Index was outside the bounds of the array.) (Index was outside the bounds of the array.) (Index was outside the bounds of the array.) ---> System.IndexOutOfRangeException: Index was outside the bounds of the array.
  at Morpheus.AminoAcidMasses.GetMonoisotopicMass (System.Char aminoAcid) [0x00000] in <c19cd36571be4e1c82621f0bf4b72e61>:0 
  at Morpheus.AminoAcidPolymer.get_MonoisotopicMass () [0x00020] in <c19cd36571be4e1c82621f0bf4b72e61>:0 
  at Morpheus.DatabaseSearcher+<DoSearch>c__AnonStorey1.<>m__0 (Morpheus.Protein protein) [0x001b2] in <c19cd36571be4e1c82621f0bf4b72e61>:0 
  at System.Threading.Tasks.Parallel+<>c__DisplayClass44_0`2[TSource,TLocal].<PartitionerForEachWorker>b__1 (System.Collections.IEnumerator& partitionState, System.Int32 timeout, System.Boolean& replicationDelegateYieldedBeforeCompletion) [0x0010f] in <6e26a535bf76467f9082042847cb7d56>:0 

  ```

  It looks like Morpheus is not able to process unconventional amino acid characters in the database?


## Conclusion
?
