## ---------------------------------------------------------------------------
## Created on: 
## Description: 
## This program was created/modified by Daniel M. Sheehan at the Built 
## Environment and Health Project (beh.columbia.edu) of Department of Epidemiology at Columbia University
## Contact Info: dms2203@columbia.edu 
## Project Info: NETS King County
## -----------------------------------------------------------------------------------------------------------------

import pandas as pd
import csv

#W = "W:"
W = "/Users/danielmsheehan/Dropbox"

in_path = W + "/GIS/Projects/king_county/data/input"
work_path = W + "/GIS/Projects/king_county/data/processing"
path = W + "/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_"
pr_path = W + "/GIS/Projects/king_county/data/processing"
cy_path = W + "/GIS/Projects/king_county/data/processing/tables/censusyear_list/"

geogs = ["5km", "pol"]
ctypes = ["raw", "col"]
g_abbrevs = ["b","t"]
flag_abbrevs = ["NOT_OV","BAR_OV","LIQ_OV","FSH_OV","FVM_OV","NAT_OV","MET_OV","SMK_OV","EAT_OV","CON_OV","AFF_OV","PIZ_OV","BAK_OV","BNK_OV","CRD_OV","MUL_OV","LMPA_OV","VPA_OV","WARE_OV","DES_OV","URG_OV","HP_OV","RES_OV","RX_OV","MH_OV","DDS_OV"]

a = pd.read_csv(cy_path + "census_list.txt")

print "For Tract Polygon Raw and Collapsed Counts; then Tract Centroid 5km Buffer Raw and Collapsed Counts"
for geog in geogs:
	for year in range(1990,2011):
		#for flag, flag_abbrev in zip(range(26), flag_abbrevs):
		b = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_0_both_clean.txt")

		merged = pd.merge(a, b, how='left', on='tractid')

		def_file_1 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_1_both_clean.txt")
		def_file_2 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_2_both_clean.txt")
		def_file_3 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_3_both_clean.txt")
		def_file_4 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_4_both_clean.txt")
		def_file_5 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_5_both_clean.txt")
		def_file_6 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_6_both_clean.txt")
		def_file_7 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_7_both_clean.txt")
		def_file_8 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_8_both_clean.txt")
		def_file_9 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_9_both_clean.txt")
		def_file_10 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_10_both_clean.txt")
		def_file_11 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_11_both_clean.txt")
		def_file_12 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_12_both_clean.txt")
		def_file_13 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_13_both_clean.txt")
		def_file_14 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_14_both_clean.txt")
		def_file_15 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_15_both_clean.txt")
		def_file_16 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_16_both_clean.txt")
		def_file_17 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_17_both_clean.txt")
		def_file_18 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_18_both_clean.txt")
		def_file_19 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_19_both_clean.txt")
		def_file_20 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_20_both_clean.txt")
		def_file_21 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_21_both_clean.txt")
		def_file_22 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_22_both_clean.txt")
		def_file_23 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_23_both_clean.txt")
		def_file_24 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_24_both_clean.txt")
		def_file_25 = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_25_both_clean.txt")

		allmerged1 = merged.merge(def_file_1, how='left', on='tractid')

		allmerged2 = allmerged1.merge(def_file_2, how='left', on='tractid').merge(def_file_3, how='left', on='tractid').merge(def_file_4, how='left', on='tractid').merge(def_file_5, how='left', on='tractid').merge(def_file_6, how='left', on='tractid').merge(def_file_7, how='left', on='tractid').merge(def_file_8, how='left', on='tractid').merge(def_file_9, how='left', on='tractid').merge(def_file_10, how='left', on='tractid').merge(def_file_11, how='left', on='tractid').merge(def_file_12, how='left', on='tractid').merge(def_file_13, how='left', on='tractid').merge(def_file_14, how='left', on='tractid').merge(def_file_15, how='left', on='tractid').merge(def_file_16, how='left', on='tractid').merge(def_file_17, how='left', on='tractid').merge(def_file_18, how='left', on='tractid').merge(def_file_19, how='left', on='tractid').merge(def_file_20, how='left', on='tractid').merge(def_file_21, how='left', on='tractid').merge(def_file_22, how='left', on='tractid').merge(def_file_23, how='left', on='tractid').merge(def_file_24, how='left', on='tractid').merge(def_file_25, how='left', on='tractid')

		allmerged2.to_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_" + geog + "_" + str(year) + "_final.txt", index=False)

	#print allmerged

print "merge Tract Polygon and Tract Centroid 5 km Buffer Tables"
for year in range(1990,2011):

		b = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_pol_" + str(year) + "_final.txt")
		c = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/_out/kc_nets_5km_" + str(year) + "_final.txt")

		merged = pd.merge(a, b, how='left', on='tractid')

		allmerged = merged.merge(c, how='left', on='tractid')

		allmerged.to_csv(pr_path + "/tables/nets_year_flag_tables/_final/kc_nets_" + str(year) + "_final.txt", index=False)




