import os
import errno
import re, urllib, time, zipfile, os
import arcpy
from arcpy import env
env.overwriteOutput = True

#################################################
### THIS IS THE ONLY THING YOU NEED TO MODIFY ###
#################################################
#put your file location here between quotes ie. 
folder_path = "W:/GIS/Projects/king_county/data/processing/tables"
#################################################
### THIS IS THE ONLY THING YOU NEED TO MODIFY ###
#################################################

print 'Started entire script at this time: ' + time.strftime('%c') 

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

the_foldernames = ["census_geographies","utm_xy_round","land_area","census_uw_vars","nets_intersects","census_data"]

for var in the_foldernames:
	make_sure_path_exists(folder_path+"/"+var)
