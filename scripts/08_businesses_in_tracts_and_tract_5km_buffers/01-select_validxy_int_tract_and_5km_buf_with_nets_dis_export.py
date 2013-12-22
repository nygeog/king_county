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
arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

in_path = "W:/GIS/Projects/king_county/data/input"
work_path = "W:/GIS/Projects/king_county/data/processing"
path = "W:/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_"
pr_path = "W:/GIS/Projects/king_county/data/processing"
cy_path = "W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/"

geogs = ["5km", "pol"]
g_abbrevs = ["b","t"]
flag_abbrevs = ["NOT_OV","BAR_OV","LIQ_OV","FSH_OV","FVM_OV","NAT_OV","MET_OV","SMK_OV","EAT_OV","CON_OV","AFF_OV","PIZ_OV","BAK_OV","BNK_OV","CRD_OV","MUL_OV","LMPA_OV","VPA_OV","WARE_OV","DES_OV","URG_OV","HP_OV","RES_OV","RX_OV","MH_OV","DDS_OV"]

#Processing intersects, clips, etc. 
#-----------------------------------------------------------------------------------------------------------------


print 'select valid nets xy and final_accuracy (50 seconds)'
print 'start: ' + time.strftime('%c') 
#REMOVE #arcpy.Select_analysis(work_path+"/nets_tract_intersects.gdb/king_county_pts",work_path+"/nets_tract_intersects.gdb/king_county_pts_valid_xy","POINT_X > 0 AND POINT_Y > 0 AND final_accuracy <> 'Z'")
print 'clip nets by king county polygon (35 seconds)'
print 'start: ' + time.strftime('%c') 
#REMOVE AS WELL #arcpy.Clip_analysis(work_path+"/nets_tract_intersects.gdb/king_county_pts_restricted_final_accuracy_pts",in_path+"/census.gdb/tracts_2000_king_county",work_path+"/nets_tract_intersects.gdb/king_county_pts_restricted_valid_xy_king_county","#")

print 'intersect tracts and businesses (nets) (1 minute)'
print 'start: ' + time.strftime('%c') 
arcpy.Intersect_analysis(work_path+"/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000 #;"                 +work_path+"/nets_tract_intersects.gdb/king_county_pts_restricted_final_accuracy_pts #",work_path+"/nets_tract_intersects.gdb/utm_z10n/tract_pol_nets_int","ALL","#","INPUT")
print 'intersect tract - centroid 5 km buffer and businesses (nets) (17 minutes)'
print 'start: ' + time.strftime('%c') 
arcpy.Intersect_analysis(work_path+"/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000_centroid_5km_buf #;"+work_path+"/nets_tract_intersects.gdb/king_county_pts_restricted_final_accuracy_pts #",work_path+"/nets_tract_intersects.gdb/utm_z10n/tract_5km_nets_int","ALL","#","INPUT")

# Selects and Table processing
# -----------------------------------------------------------------------------------------------------------------

print 'select by year and flag, dissolve for both, (took 16 hours for buffers and 3 hours for tracts)'
print 'start: ' + time.strftime('%c') 
for geog in geogs:
	for year in range(1990,2011,1):
		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
			sqlexp = "BEH_" + str(year) + " = 1 AND " + flag_abbrev + " = 1"
			arcpy.Select_analysis    (work_path+"/nets_tract_intersects.gdb/utm_z10n/tract_" + geog + "_nets_int", work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) , sqlexp)
			arcpy.Dissolve_management(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag),                        work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid",                    "tractid",           flag_abbrev + " SUM",             "MULTI_PART","DISSOLVE_LINES")
			arcpy.Dissolve_management(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag),                        work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround",            "tractid;xyrounduid",flag_abbrev + " COUNT",           "MULTI_PART","DISSOLVE_LINES")
			arcpy.Dissolve_management(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround",work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround_dis_tractid","tractid",           "COUNT_" + flag_abbrev + " COUNT","MULTI_PART","DISSOLVE_LINES")
			print "done with kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround AT - " + time.strftime('%c') 


print 'deleting intermediate files '
print 'start: ' + time.strftime('%c') 
for geog in geogs:
	for year in range(1990,2011,1):
		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
			print 'deleting intermediate file: '+ work_path + "/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround"
			arcpy.Delete_management(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround")


#TURN THIS ON TO EXPORT BUT FIRST GONNA NEED TO DELETE ALL THE OUTPUT AS DOESN'T OVERWRITE BY DEFAULT

print "make table views of censusyear list tables for each year and join tables of all business types, table to table (next loop is export to .txt)"
print 'start: ' + time.strftime('%c') 
for geog in geogs:
	for year in range(1990,2011):
		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
			arcpy.XToolsGP_Export2Text(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid",                     "tractid;SUM_" +         flag_abbrev, work_path + "/tables/nets_year_flag_tables/working/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_raw.txt","false","false")
			arcpy.XToolsGP_Export2Text(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_dis_tractid_xyround_dis_tractid", "tractid;COUNT_COUNT_" + flag_abbrev, work_path + "/tables/nets_year_flag_tables/working/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) +"_col.txt","false","false")








