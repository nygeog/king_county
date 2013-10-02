import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True



arcpy.TableToTable_conversion("E:/Dropbox/GIS/Projects/king_county/data/input/kco_regeocode_bygooglemap/kco_regeocode_bygooglemap.csv","E:/Dropbox/GIS/Projects/king_county/data/processing/king_county.gdb","king_county_table","#","#","#")



print 'Script ended at this time: ' + time.strftime('%c') 
raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 