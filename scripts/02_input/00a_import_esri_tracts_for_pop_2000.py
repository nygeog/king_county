import arcpy

arcpy.Select_analysis("V:/Dropbox/GIS/Data/Esri/Data_and_Maps_10-1/usa/census/tracts.sdc/tracts","V:/Dropbox/GIS/Projects/king_county/data/input/census.gdb/tracts_2000_esri",""""STCOFIPS" = '53033'""")