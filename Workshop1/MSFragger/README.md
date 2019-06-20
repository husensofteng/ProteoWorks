# MSFragger
> Ultrafast and comrehensive peptide identification in ms based proteomics

Group members: Tanvir, Mattias, Taner

## Paramters
database_name = /Users/tanerarslan/Desktop/bioinfo_workshop/Human_Ecoli_target.fa
num_threads = 0			# 0=poll CPU to set num threads; else specify num threads directly (max 64)

precursor_mass_lower = -10
precursor_mass_upper = 10
precursor_mass_units = 1			# 0=Daltons, 1=ppm
precursor_true_tolerance = 0
precursor_true_units = 0			# 0=Daltons, 1=ppm
fragment_mass_tolerance = 0.02
fragment_mass_units = 0			# 0=Daltons, 1=ppm
calibrate_mass = 2			# 0=Off, 1=On, 2=On and find optimal parameters
decoy_prefix = rev_

isotope_error = 0/1/2			# 0=off, -1/0/1/2/3 (standard C13 error)
mass_offsets = 0			# allow for additional precursor mass window shifts. Multiplexed with isotope_error. mass_offsets = 0/79.966 can be used as a restricted ‘open’ search that looks for unmodified and phosphorylated peptides (on any residue)
precursor_mass_mode = selected

localize_delta_mass = 0
delta_mass_exclude_ranges = (-1.5,3.5)
fragment_ion_series = b,y

search_enzyme_name = Trypsin
search_enzyme_cutafter = KR
search_enzyme_butnotafter = P

num_enzyme_termini = 2			# 2 for enzymatic, 1 for semi-enzymatic, 0 for nonspecific digestion
allowed_missed_cleavage = 1			# maximum value is 5

clip_nTerm_M = 1

###maximum of 7 mods - amino acid codes, * for any amino acid, [ and ] specifies protein termini, n and c specifies peptide termini
variable_mod_01 = 15.99490 M
### variable_mod_02 = 42.01060 [^
### variable_mod_03 = 79.96633 STY
### variable_mod_04 = -17.02650 nQnC
### variable_mod_05 = -18.01060 nE
### variable_mod_06 = 0.00000 site_06
### variable_mod_07 = 0.00000 site_07

allow_multiple_variable_mods_on_residue = 1			# static mods are not considered
max_variable_mods_per_mod = 3			# maximum of 5
max_variable_mods_combinations = 5000			# maximum of 65534, limits number of modified peptides generated from sequence

output_file_extension = pepXML
output_format = tsv_pepXML
output_report_topN = 1
output_max_expect = 50
report_alternative_proteins = 0			# 0=no, 1=yes

precursor_charge = 2 6			# precursor charge range to analyze; does not override any existing charge; 0 as 1st entry ignores parameter
override_charge = 1			# 0=no, 1=yes to override existing precursor charge states with precursor_charge parameter

digest_min_length = 7
digest_max_length = 50
digest_mass_range = 500.0 6000.0			# MH+ peptide mass range to analyze
max_fragment_charge = 2			# set maximum fragment charge state to analyze (allowed max 5)

####open search parameters
track_zero_topN = 0			# in addition to topN results, keep track of top results in zero bin
zero_bin_accept_expect = 0.00			# boost top zero bin entry to top if it has expect under 0.01 - set to 0 to disable
zero_bin_mult_expect = 1.00			# disabled if above passes - multiply expect of zero bin for ordering purposes (does not affect reported expect)
add_topN_complementary = 0

####spectral processing

minimum_peaks = 15			# required minimum number of peaks in spectrum to search (default 10)
use_topN_peaks = 150
min_fragments_modelling = 2
min_matched_fragments = 4
minimum_ratio = 0.01			# filter peaks below this fraction of strongest peak
clear_mz_range = 0.0 0.0			# for iTRAQ/TMT type data; will clear out all peaks in the specified m/z range

####additional modifications

add_Cterm_peptide = 0.000000
add_Nterm_peptide = 229.162932
add_Cterm_protein = 0.000000
add_Nterm_protein = 0.000000

add_G_glycine = 0.000000
add_A_alanine = 0.000000
add_S_serine = 0.000000
add_P_proline = 0.000000
add_V_valine = 0.000000
add_T_threonine = 0.000000
add_C_cysteine = 57.021464
add_L_leucine = 0.000000
add_I_isoleucine = 0.000000
add_N_asparagine = 0.000000
add_D_aspartic_acid = 0.000000
add_Q_glutamine = 0.000000
add_K_lysine = 229.162932
add_E_glutamic_acid = 0.000000
add_M_methionine = 0.000000
add_H_histidine = 0.000000
add_F_phenylalanine = 0.000000
add_R_arginine = 0.000000
add_Y_tyrosine = 0.000000
add_W_tryptophan = 0.000000
add_B_user_amino_acid = 0.000000
add_J_user_amino_acid = 0.000000
add_O_user_amino_acid = 0.000000
add_U_user_amino_acid = 0.000000
add_X_user_amino_acid = 0.000000
add_Z_user_amino_acid = 0.000000




## Run
java -jar bin/MSFragger-20190530.jar params/fragger.params *.mzML
