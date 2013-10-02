import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

dir_loc = r'E:\Dropbox\GIS\Projects\king_county\data'
pts = r'E:\Dropbox\GIS\Projects\king_county\data\processing\king_county.gdb\king_county_pts'
dir_out = r'E:\Dropbox\GIS\Projects\king_county\data\processing\intersects.gdb'

print "create xy event layer - note that x and y in stata file are reversed - so switch if updated"
arcpy.MakeXYEventLayer_management(dir_loc+"/processing/king_county.gdb/king_county_table","final_y","final_x","king_county_table_layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")

print "project to utm zone 10"
arcpy.Project_management("king_county_table_layer",pts,"PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]")

print "start Spatial Joins not gonna comment much" + time.strftime('%c')
arcpy.SpatialJoin_analysis(pts,dir_loc+"/input/census.gdb/tracts_1990",dir_out+"/king_county_tract_1990_sp","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT","0 Meters","#")
arcpy.SpatialJoin_analysis(pts,dir_loc+"/input/census.gdb/tracts_2000",dir_out+"/king_county_tract_2000_sp","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT","0 Meters","#")
arcpy.SpatialJoin_analysis(pts,dir_loc+"/input/census.gdb/tracts_2010",dir_out+"/king_county_tract_2010_sp","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT","0 Meters","#")
arcpy.SpatialJoin_analysis(pts,dir_loc+"/input/census.gdb/zcta_2000"  ,dir_out+"/king_county_zcta_2000_sp","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT","0 Meters","#")
arcpy.SpatialJoin_analysis(pts,dir_loc+"/input/census.gdb/zcta_2010"  ,dir_out+"/king_county_zcta_2010_sp","JOIN_ONE_TO_ONE","KEEP_ALL","","INTERSECT","0 Meters","#")

print "start Add Fields not gonna comment much" + time.strftime('%c')
arcpy.AddField_management(dir_out+"/king_county_tract_1990_sp","g_ct1990","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(dir_out+"/king_county_tract_2000_sp","g_ct2000","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(dir_out+"/king_county_tract_2010_sp","g_ct2010","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(dir_out+"/king_county_zcta_2000_sp", "g_zt2000","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(dir_out+"/king_county_zcta_2010_sp", "g_zt2010","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

print "start Calc Fields not gonna comment much" + time.strftime('%c')
arcpy.CalculateField_management(dir_out+"/king_county_tract_1990_sp","g_ct1990","!geoid_beh!","PYTHON_9.3","#")
arcpy.CalculateField_management(dir_out+"/king_county_tract_2000_sp","g_ct2000","!CTIDFP00!", "PYTHON_9.3","#")
arcpy.CalculateField_management(dir_out+"/king_county_tract_2010_sp","g_ct2010","!GEOID10!",  "PYTHON_9.3","#")
arcpy.CalculateField_management(dir_out+"/king_county_zcta_2000_sp","g_zt2000", "!ZCTA5CE00!","PYTHON_9.3","#")
arcpy.CalculateField_management(dir_out+"/king_county_zcta_2010_sp","g_zt2010", "!ZCTA5CE10!","PYTHON_9.3","#")

#check if csvs are already there, if so delete

arcpy.XToolsPro_Table2Text(dir_loc+"/processing/intersects.gdb/king_county_tract_1990_sp","BEH_ID;g_ct1990",dir_loc+"/processing/tables/ct1990.csv")
arcpy.XToolsPro_Table2Text(dir_loc+"/processing/intersects.gdb/king_county_tract_2000_sp","BEH_ID;g_ct2000",dir_loc+"/processing/tables/ct2000.csv")
arcpy.XToolsPro_Table2Text(dir_loc+"/processing/intersects.gdb/king_county_tract_2010_sp","BEH_ID;g_ct2010",dir_loc+"/processing/tables/ct2010.csv")
arcpy.XToolsPro_Table2Text(dir_loc+"/processing/intersects.gdb/king_county_zcta_2000_sp", "BEH_ID;g_zt2000",dir_loc+"/processing/tables/zt2000.csv")
arcpy.XToolsPro_Table2Text(dir_loc+"/processing/intersects.gdb/king_county_zcta_2010_sp", "BEH_ID;g_zt2010",dir_loc+"/processing/tables/zt2010.csv")

print 'Script ended at this time: ' + time.strftime('%c') 
raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 