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

in_path = "W:/GIS/Projects/king_county/data/input"
work_path = "W:/GIS/Projects/king_county/data/processing"
path = "W:/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_"
pr_path = "W:/GIS/Projects/king_county/data/processing"
cy_path = "W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/"

geogs = ["5km", "pol"]
g_abbrevs = ["b","t"]
flag_abbrevs = ["NOT_OV","BAR_OV","LIQ_OV","FSH_OV","FVM_OV","NAT_OV","MET_OV","SMK_OV","EAT_OV","CON_OV","AFF_OV","PIZ_OV","BAK_OV","BNK_OV","CRD_OV","MUL_OV","LMPA_OV","VPA_OV","WARE_OV","DES_OV","URG_OV","HP_OV","RES_OV","RX_OV","MH_OV","DDS_OV"]

# Processing intersects, clips, etc. 
# -----------------------------------------------------------------------------------------------------------------
# print 'select valid nets xy and final_accuracy (50 seconds)'
# print 'start: ' + time.strftime('%c') 
# arcpy.Select_analysis(work_path+"/nets_king_county.gdb/king_county_pts",work_path+"/nets_king_county.gdb/king_county_pts_valid_xy","POINT_X > 0 AND POINT_Y > 0 AND final_accuracy <> 'Z'")
# print 'clip nets by king county polygon (35 seconds)'
# print 'start: ' + time.strftime('%c') 
# arcpy.Clip_analysis(work_path+"/nets_king_county.gdb/king_county_pts_valid_xy",in_path+"/census.gdb/tracts_2000_king_county",work_path+"/nets_king_county.gdb/king_county_pts_valid_xy_king_county","#")

# print 'intersect tracts and businesses (nets) (1 minute)'
# print 'start: ' + time.strftime('%c') 
# arcpy.Intersect_analysis(work_path+"/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000 #;"                 +work_path+"/nets_king_county.gdb/king_county_pts_valid_xy_king_county #",work_path+"/nets_tract_intersects.gdb/utm_z10n/tract_pol_nets_int","ALL","#","INPUT")
# print 'intersect tract - centroid 5 km buffer and businesses (nets) (17 minutes)'
# print 'start: ' + time.strftime('%c') 
# arcpy.Intersect_analysis(work_path+"/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000_centroid_5km_buf #;"+work_path+"/nets_king_county.gdb/king_county_pts_valid_xy_king_county #",work_path+"/nets_tract_intersects.gdb/utm_z10n/tract_5km_nets_int","ALL","#","INPUT")

# Selects and Table processing
# -----------------------------------------------------------------------------------------------------------------

print 'select by year and flag '
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




# #dissolves

# print 'select by year and flag '
# print 'start: ' + time.strftime('%c') 
# for geog in geogs:
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):









# print 'frequency tables of biz types - raw count'
# print 'start: ' + time.strftime('%c')
# for geog in geogs:
# 	for year in range(1990,2011,1):
# 		arcpy.Frequency_analysis(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year), work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_raw","tractid","NOT_OV;BAR_OV;LIQ_OV;FSH_OV;FVM_OV;NAT_OV;MET_OV;SMK_OV;EAT_OV;CON_OV;AFF_OV;PIZ_OV;BAK_OV;BNK_OV;CRD_OV;MUL_OV;LMPA_OV;VPA_OV;WARE_OV;DES_OV;URG_OV;HP_OV;RES_OV;RX_OV;MH_OV;DDS_OV")

# print 'frequency tables of biz types - collapsed count'
# print 'start: ' + time.strftime('%c')
# for geog in geogs:
# 	for year in range(1990,2011,1):







# print 'frequency tables of biz types - collapsed count'
# print 'start: ' + time.strftime('%c')
# for geog in geogs:
# 	for year in range(1990,2011,1):
# 		arcpy.Frequency_analysis(work_path+"/nets_year_flag_select.gdb/kc_nets_" + geog + "_" + str(year), work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_col_pre","tractid;xyrounduid","NOT_OV;BAR_OV;LIQ_OV;FSH_OV;FVM_OV;NAT_OV;MET_OV;SMK_OV;EAT_OV;CON_OV;AFF_OV;PIZ_OV;BAK_OV;BNK_OV;CRD_OV;MUL_OV;LMPA_OV;VPA_OV;WARE_OV;DES_OV;URG_OV;HP_OV;RES_OV;RX_OV;MH_OV;DDS_OV")

# print 'frequency tables of biz types - finish collapsed count'
# print 'start: ' + time.strftime('%c')
# for geog in geogs:
# 	for year in range(1990,2011,1):
# 		arcpy.Frequency_analysis(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_col_pre", work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_col","tractid","NOT_OV;BAR_OV;LIQ_OV;FSH_OV;FVM_OV;NAT_OV;MET_OV;SMK_OV;EAT_OV;CON_OV;AFF_OV;PIZ_OV;BAK_OV;BNK_OV;CRD_OV;MUL_OV;LMPA_OV;VPA_OV;WARE_OV;DES_OV;URG_OV;HP_OV;RES_OV;RX_OV;MH_OV;DDS_OV")






# print 'add business type count field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.AddField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_raw", g_abbrev + "n" + flag_abbrev + "raw","LONG","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# print 'calc business type count field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.CalculateField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq", g_abbrev + "n" + flag_abbrev + "raw","!" + flag_abbrev + "!","PYTHON_9.3","#")

# print 'add year field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.AddField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq", "year","LONG","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# print 'calc year field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.CalculateField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq", "year", year, "PYTHON_9.3","#")

# print 'add censusyear field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.AddField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq", "censusyear","STRING","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# print 'calc censusyear field'
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.CalculateField_management(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq", "censusyear", "str(!tractid!) + str(!year!)", "PYTHON_9.3","#")

# print "make table views of censusyear list tables for each year and join tables of all business types, table to table (next loop is export to .txt)"
# for year in range(1990,2011):
# 	arcpy.MakeTableView_management(cy_path + "censusyear_list.gdb/censusyear_list","censusyear_list_view_" + str(year),"censusyear LIKE '%" + str(year) +"'","#","OBJECTID OBJECTID VISIBLE NONE;censusyear censusyear VISIBLE NONE")
# 	for geog in geogs:
# 		for bizflagnum, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.AddJoin_management("censusyear_list_view_" + str(year),"censusyear",pr_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(bizflagnum) + "_freq","censusyear","KEEP_ALL")

# 	arcpy.TableToTable_conversion("censusyear_list_view_" + str(year), cy_path + "censusyear_list.gdb","censusyear_list_" + str(year) + "_vars","#","#","#")

# print "export yearly tables to .txt with xtools"
# arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')
# for yearInt in range(1990,2011):
# 	year = str(yearInt)
# 	arcpy.XToolsGP_Export2Text(cy_path + "censusyear_list.gdb/censusyear_list_" + year + "_vars","censusyear;kc_nets_5km_" + year + "_0_freq_bnNOT_OVraw;kc_nets_5km_" + year + "_1_freq_bnBAR_OVraw;kc_nets_5km_" + year + "_2_freq_bnLIQ_OVraw;kc_nets_5km_" + year + "_3_freq_bnFSH_OVraw;kc_nets_5km_" + year + "_4_freq_bnFVM_OVraw;kc_nets_5km_" + year + "_5_freq_bnNAT_OVraw;kc_nets_5km_" + year + "_6_freq_bnMET_OVraw;kc_nets_5km_" + year + "_7_freq_bnSMK_OVraw;kc_nets_5km_" + year + "_8_freq_bnEAT_OVraw;kc_nets_5km_" + year + "_9_freq_bnCON_OVraw;kc_nets_5km_" + year + "_10_freq_bnAFF_OVraw;kc_nets_5km_" + year + "_11_freq_bnPIZ_OVraw;kc_nets_5km_" + year + "_12_freq_bnBAK_OVraw;kc_nets_5km_" + year + "_13_freq_bnBNK_OVraw;kc_nets_5km_" + year + "_14_freq_bnCRD_OVraw;kc_nets_5km_" + year + "_15_freq_bnMUL_OVraw;kc_nets_5km_" + year + "_16_freq_bnLMPA_OVraw;kc_nets_5km_" + year + "_17_freq_bnVPA_OVraw;kc_nets_5km_" + year + "_18_freq_bnWARE_OVraw;kc_nets_5km_" + year + "_19_freq_bnDES_OVraw;kc_nets_5km_" + year + "_20_freq_bnURG_OVraw;kc_nets_5km_" + year + "_21_freq_bnHP_OVraw;kc_nets_5km_" + year + "_22_freq_bnRES_OVraw;kc_nets_5km_" + year + "_23_freq_bnRX_OVraw;kc_nets_5km_" + year + "_24_freq_bnMH_OVraw;kc_nets_5km_" + year + "_25_freq_bnDDS_OVraw;kc_nets_pol_" + year + "_0_freq_tnNOT_OVraw;kc_nets_pol_" + year + "_1_freq_tnBAR_OVraw;kc_nets_pol_" + year + "_2_freq_tnLIQ_OVraw;kc_nets_pol_" + year + "_3_freq_tnFSH_OVraw;kc_nets_pol_" + year + "_4_freq_tnFVM_OVraw;kc_nets_pol_" + year + "_5_freq_tnNAT_OVraw;kc_nets_pol_" + year + "_6_freq_tnMET_OVraw;kc_nets_pol_" + year + "_7_freq_tnSMK_OVraw;kc_nets_pol_" + year + "_8_freq_tnEAT_OVraw;kc_nets_pol_" + year + "_9_freq_tnCON_OVraw;kc_nets_pol_" + year + "_10_freq_tnAFF_OVraw;kc_nets_pol_" + year + "_11_freq_tnPIZ_OVraw;kc_nets_pol_" + year + "_12_freq_tnBAK_OVraw;kc_nets_pol_" + year + "_13_freq_tnBNK_OVraw;kc_nets_pol_" + year + "_14_freq_tnCRD_OVraw;kc_nets_pol_" + year + "_15_freq_tnMUL_OVraw;kc_nets_pol_" + year + "_16_freq_tnLMPA_OVraw;kc_nets_pol_" + year + "_17_freq_tnVPA_OVraw;kc_nets_pol_" + year + "_18_freq_tnWARE_OVraw;kc_nets_pol_" + year + "_19_freq_tnDES_OVraw;kc_nets_pol_" + year + "_20_freq_tnURG_OVraw;kc_nets_pol_" + year + "_21_freq_tnHP_OVraw;kc_nets_pol_" + year + "_22_freq_tnRES_OVraw;kc_nets_pol_" + year + "_23_freq_tnRX_OVraw;kc_nets_pol_" + year + "_24_freq_tnMH_OVraw;kc_nets_pol_" + year + "_25_freq_tnDDS_OVraw", pr_path + "/tables/nets_intersects/kc_nets_" + year + "_biz_raw.txt", "false","true")













# the loop thing

# 			make layer (grab that .dta list of census year )





# geogs = ["5km", "pol"]
# g_abbrevs = ["b","t"]
# flag_abbrevs = ["NOT_OV","BAR_OV","LIQ_OV","FSH_OV","FVM_OV","NAT_OV","MET_OV","SMK_OV","EAT_OV","CON_OV","AFF_OV","PIZ_OV","BAK_OV","BNK_OV","CRD_OV","MUL_OV","LMPA_OV","VPA_OV","WARE_OV","DES_OV","URG_OV","HP_OV","RES_OV","RX_OV","MH_OV","DDS_OV"]
# for geog, g_abbrev in zip(geogs, g_abbrevs):
# 	for year in range(1990,2011,1):
# 		for flag, flag_abbrev in zip(range(26), flag_abbrevs):
# 			arcpy.XToolsGP_Export2Text(work_path + "/nets_year_flag_tables.gdb/kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq","tractid;" + g_abbrev + "n" + flag_abbrev + "raw;year", work_path + "/tables/nets_year_flag_tables/" + "kc_nets_" + geog + "_" + str(year) + "_" + str(flag) + "_freq_raw.txt","false","false")


