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

print "For Tract Polygon Raw and Collapsed Counts"
for year in range(1990,2011):
	for flag, flag_abbrev in zip(range(26), flag_abbrevs):
		b = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/working/kc_nets_pol_" + str(year) + "_" + str(flag) + "_raw.txt")

		merged = pd.merge(a, b, how='left', on='tractid')

		def_file = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/working/kc_nets_pol_" + str(year) + "_" + str(flag) + "_col.txt")
		allmerged = merged.merge(def_file, how='left', on='tractid')

		allmerged.to_csv(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_pol_" + str(year) + "_" + str(flag) + "_both.txt", index=False)

		print allmerged

		fin = csv.reader(open(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_pol_" + str(year) + "_" + str(flag) + "_both.txt", 'rb'), delimiter=',')
		fout = open(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_pol_" + str(year) + "_" + str(flag) + "_both_clean.txt", 'w')

		for row in fin:
  			for item, i in zip(row, range(3)):
				str_row = item   
				fout.write(str_row.replace('SUM_' + flag_abbrev,'tn_' + flag_abbrev + '_raw').replace('COUNT_COUNT_' + flag_abbrev,'tn_' + flag_abbrev + '_col'))
				if i < 2:
					fout.write(",")
				else:
					fout.write("")
			fout.write("\n")

		fout.close()

print "For Tract Centroid 5 km Buffer Raw and Collapsed Counts"
for year in range(1990,2011):
	for flag, flag_abbrev in zip(range(26), flag_abbrevs):
		b = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/working/kc_nets_5km_" + str(year) + "_" + str(flag) + "_raw.txt")

		merged = pd.merge(a, b, how='left', on='tractid')

		def_file = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/working/kc_nets_5km_" + str(year) + "_" + str(flag) + "_col.txt")
		allmerged = merged.merge(def_file, how='left', on='tractid')

		allmerged.to_csv(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_5km_" + str(year) + "_" + str(flag) + "_both.txt", index=False)

		print allmerged

		fin = csv.reader(open(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_5km_" + str(year) + "_" + str(flag) + "_both.txt", 'rb'), delimiter=',')
		fout = open(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_5km_" + str(year) + "_" + str(flag) + "_both_clean.txt", 'w')

		for row in fin:
  			for item, i in zip(row, range(3)):
				str_row = item  
				fout.write(str_row.replace('SUM_' + flag_abbrev,'bn_' + flag_abbrev + '_raw').replace('COUNT_COUNT_' + flag_abbrev,'bn_' + flag_abbrev + '_col'))
				if i < 2:
					fout.write(",")
				else:
					fout.write("")
			fout.write("\n")

		fout.close()

	
















# merged = pd.merge(a, b, how='left', on='title')
#         def_file = pd.read_csv(pr_path + "/tables/nets_year_flag_tables/kc_nets_pol" + )
#         allmerged = merged.merge(def_file, how='left', on='title')

#print allmerged
#allmerged.to_csv(pr_path + "/tables/nets_year_flag_tables/out/kc_nets_pol.txt", index=False)

