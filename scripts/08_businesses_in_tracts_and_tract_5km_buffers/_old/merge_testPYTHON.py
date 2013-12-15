import csv
import pandas as pd

proj_path = '/Users/danielmsheehan/Dropbox/GIS/Projects/king_county/data/processing/tables/nets_year_flag_tables/'
outp_path = '/Users/danielmsheehan/Dropbox/GIS/Projects/king_county/data/processing/tables/nets_year_flag_tables_stata/'

a = pd.read_csv(outp_path + "kc_nets_5km_1990_0_freq_raw.txt") # + str(year) + "_" + str(flag) + "_freq_raw.txt")
b = pd.read_csv(outp_path + "kc_nets_5km_1990_1_freq_raw.txt") #" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.txt")
b = b.dropna(axis=1)
merged = a.merge(b, on='censusyear')
merged.to_csv(outp_path + "TEST.csv", index=False) #"kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.csv", index=False)