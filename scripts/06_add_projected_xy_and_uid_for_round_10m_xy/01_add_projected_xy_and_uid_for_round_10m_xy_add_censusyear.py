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
arcpy.AddField_management(the_file, "xyrounduid", "STRING")
arcpy.CalculateField_management(the_file, "xyrounduid", "str(!x_round!) + '^' + str(!y_round!)" ,"PYTHON_9.3","#")



#THIS IS NOT 10.2 compatible (iMac use arcpy.XToolsGP_Export2Text()
arcpy.XToolsPro_Table2Text(the_file,"BEH_ID;POINT_X;POINT_Y;x_round;y_round;xyrounduid",file_loc+"/data/processing/tables/utm_xy_round/utm_xy_round.txt")