import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

file_loc = "W:/GIS/Projects/king_county"

the_file = file_loc + "/data/processing/nets_king_county.gdb/king_county_pts"

#the_file2 = r'Y:\Dropbox\GIS\Projects\king_county\data\processing\king_county.gdb\king_county_pts'

arcpy.AddXY_management(the_file)
arcpy.AddField_management(the_file,"x_round","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(the_file,"y_round","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(the_file,"x_round","round( !POINT_X! , -1)","PYTHON_9.3","#")
arcpy.CalculateField_management(the_file,"y_round","round( !POINT_Y! , -1)","PYTHON_9.3","#")


arcpy.XToolsGP_Export2Text(file_loc+"/data/processing/king_county.gdb/king_county_pts","BEH_ID;POINT_X;POINT_Y;x_round;y_round",file_loc+"/data/processing/tables/utm_xy_round.txt")