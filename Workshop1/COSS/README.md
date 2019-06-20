# COSS
>A fast and user-friendly tool for spectral library searching

Group members: Mohammad and Matthias


## About the search engine
- spectral library search
- probabilistic scoring function (similar to Andromeda) that includes decoy spectra generation
- available as `java` executable from GitHub

## Run
1. Download COSS from the provided link and unzip it.
2. Download `E.coli` and `H.sapiens` spectral libraries from [Pride](https://www.ebi.ac.uk/pride/cluster/#/libraries)
3. Concatenate the libraries: `cat Human.msp Escherichia_coli.msp > concat.msp`

    Then we realised: **NO MODS allowed** We need an own library including the TMT information.

4. Go on with a [TMT spectral library](http://ftp.stjude.org/pub/software/tmt/human_best_replicate.tgz) (only human).
5. CAVE: Cannot append decoy spectra with this tool because we have a `.sptxt`. Running without decoys...
6. Run for each `mzML` separately.
   
   ```java -jar COSS-1.0/COSS-1.0.jar ~/ki/bioinfo_workshop/data/GMHJYZ_DeqMSvalidation_300ug_TMT10_IPG3-10_fr07.mzML ~/ki/bioinfo_workshop/libraries/best_replicate.sptxt 10 0.02 6```

7. Quickly got a `NullPointerException`. No results available?


## Conclusion
This tool is not mature to use, yet.
