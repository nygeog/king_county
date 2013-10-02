import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')


file_loc = "V:/Dropbox/GIS/Projects/king_county"

arcpy.XToolsPro_Table2Text(file_loc+"/data/input/census.gdb/tracts_2000_king_county","CTIDFP00;ALAND00;AWATER00",file_loc+"/data/processing/tables/tracts_2000_land_water_area.csv")

arcpy.XToolsPro_Table2Text(file_loc+"/data/input/census.gdb/tracts_2000_esri","FIPS;POP2000",file_loc+"/data/processing/tables/tracts_2000_esri_pop.csv")