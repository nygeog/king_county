## ---------------------------------------------------------------------------
## Created on: 
## Description: 
## This program was created/modified by Daniel M. Sheehan at the Built 
## Environment and Health Project (beh.columbia.edu) of Department of Epidemiology at Columbia University
## Contact Info: dms2203@columbia.edu 
## Project Info: NETS King County
## -----------------------------------------------------------------------------------------------------------------

import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

## Check out any necessary licenses
#from arcpy.sa import *
#arcpy.CheckOutExtension("Network")
#arcpy.CheckOutExtension("Spatial")
#arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

inpath = "W:/GIS/Projects/king_county/data/input/census.gdb/tracts_"
path = "W:/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_"

sqls = ["ST = '53' AND CO = '033'","STATEFP00 = '53' AND COUNTYFP00 = '033'","STATEFP10 = '53' AND COUNTYFP10 = '033'"]
calcfields = ["!geoid_beh!","!CTIDFP00!", "!GEOID10!"]
years = ['1990','2000','2010']

for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.Select_analysis(inpath+year, path+year, sql)
	arcpy.AddField_management(path+year,"tractid","TEXT","#","#","15","#","NULLABLE","NON_REQUIRED","#")
	arcpy.AddField_management(path+year,"origtractarea","DOUBLE")

for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.CalculateField_management(path+year,"tractid",calcfield,"PYTHON_9.3","#")
	arcpy.CalculateField_management(path+year,"origtractarea","!shape.area@squaremeters!","PYTHON_9.3","#")
	arcpy.FeatureToPoint_management(path+year,path+year+"_centroid","INSIDE")
	arcpy.Buffer_analysis(path+year+"_centroid",path+year+"_centroid_5km_buf","5 Kilometers","FULL","ROUND","NONE","#")

for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.Intersect_analysis([path+year+"_centroid_5km_buf",path+year],path+year+"_centroid_5km_buf_int_tracts","ALL","#","INPUT")

for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.Dissolve_management(path+year+"_centroid_5km_buf_int_tracts",path+year+"_centroid_5km_buf_int_tracts_dis","tractid;origtractarea;tractid_1;origtractarea_1","#","MULTI_PART","DISSOLVE_LINES")

#for year, sql, calcfield in zip(years, sqls,calcfields):
	#arcpy.Delete_management(path+year+"_centroid_5km_buf_int_tracts","FeatureClass")
	#arcpy.Delete_management(path+year+"_centroid_5km_buf","FeatureClass")

for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.AddField_management(path+year+"_centroid_5km_buf_int_tracts_dis","newtractarea","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
	arcpy.AddField_management(path+year+"_centroid_5km_buf_int_tracts_dis","pcttractarea","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
	
for year, sql, calcfield in zip(years, sqls,calcfields):
	arcpy.CalculateField_management(path+year+"_centroid_5km_buf_int_tracts_dis","newtractarea","!shape.area@squaremeters!","PYTHON","#")
	arcpy.CalculateField_management(path+year+"_centroid_5km_buf_int_tracts_dis","pcttractarea","!newtractarea! / !origtractarea_1! ","PYTHON","#")













