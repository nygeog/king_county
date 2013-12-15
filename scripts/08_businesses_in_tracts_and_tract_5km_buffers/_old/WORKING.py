import csv
import pandas as pd

proj_path = 'W:/GIS/Projects/king_county/data/processing/tables/nets_year_flag_tables/'
outp_path = 'W:/GIS/Projects/king_county/data/processing/tables/nets_year_flag_tables_stata/'

geogs = ["5km", "pol"]
g_abbrevs = ["b","t"]
flag_abbrevs = ["NOT_OV","BAR_OV","LIQ_OV","FSH_OV","FVM_OV","NAT_OV","MET_OV","SMK_OV","EAT_OV","CON_OV","AFF_OV","PIZ_OV","BAK_OV","BNK_OV","CRD_OV","MUL_OV","LMPA_OV","VPA_OV","WARE_OV","DES_OV","URG_OV","HP_OV","RES_OV","RX_OV","MH_OV","DDS_OV"]
for geog, g_abbrev in zip(geogs, g_abbrevs):
    for year in range(1990,2011,1):
        for flag, flag_abbrev in zip(range(26), flag_abbrevs):

			a = pd.read_csv(proj_path + "kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.txt")
			b = pd.read_csv(proj_path + "kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.txt")
			b = b.dropna(axis=1)
			merged = a.merge(b, on='tractid')
			merged.to_csv(outp_path + "kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.csv", index=False)