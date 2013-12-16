arcpy.CreateFileGDB_management("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list","censusyear_list","CURRENT")

arcpy.TableToTable_conversion("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.csv","W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb","censusyear_list","#","""censusyear "censusyear" true true false 15 Text 0 0 ,First,#,W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.csv,censusyear,-1,-1""","#")

arcpy.AddField_management("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/censusyear_list","tractid","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

arcpy.CalculateField_management("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/censusyear_list","tractid","!censusyear![:11]","PYTHON_9.3","#")

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

#arcpy.XToolsGP_Export2Text(cy_path + "censusyear_list.gdb/censusyear_list_" + year + "_vars","censusyear;kc_nets_5km_" + year + "_0_freq_bnNOT_OVraw;kc_nets_5km_" + year + "_1_freq_bnBAR_OVraw;kc_nets_5km_" + year + "_2_freq_bnLIQ_OVraw;kc_nets_5km_" + year + "_3_freq_bnFSH_OVraw;kc_nets_5km_" + year + "_4_freq_bnFVM_OVraw;kc_nets_5km_" + year + "_5_freq_bnNAT_OVraw;kc_nets_5km_" + year + "_6_freq_bnMET_OVraw;kc_nets_5km_" + year + "_7_freq_bnSMK_OVraw;kc_nets_5km_" + year + "_8_freq_bnEAT_OVraw;kc_nets_5km_" + year + "_9_freq_bnCON_OVraw;kc_nets_5km_" + year + "_10_freq_bnAFF_OVraw;kc_nets_5km_" + year + "_11_freq_bnPIZ_OVraw;kc_nets_5km_" + year + "_12_freq_bnBAK_OVraw;kc_nets_5km_" + year + "_13_freq_bnBNK_OVraw;kc_nets_5km_" + year + "_14_freq_bnCRD_OVraw;kc_nets_5km_" + year + "_15_freq_bnMUL_OVraw;kc_nets_5km_" + year + "_16_freq_bnLMPA_OVraw;kc_nets_5km_" + year + "_17_freq_bnVPA_OVraw;kc_nets_5km_" + year + "_18_freq_bnWARE_OVraw;kc_nets_5km_" + year + "_19_freq_bnDES_OVraw;kc_nets_5km_" + year + "_20_freq_bnURG_OVraw;kc_nets_5km_" + year + "_21_freq_bnHP_OVraw;kc_nets_5km_" + year + "_22_freq_bnRES_OVraw;kc_nets_5km_" + year + "_23_freq_bnRX_OVraw;kc_nets_5km_" + year + "_24_freq_bnMH_OVraw;kc_nets_5km_" + year + "_25_freq_bnDDS_OVraw;kc_nets_pol_" + year + "_0_freq_tnNOT_OVraw;kc_nets_pol_" + year + "_1_freq_tnBAR_OVraw;kc_nets_pol_" + year + "_2_freq_tnLIQ_OVraw;kc_nets_pol_" + year + "_3_freq_tnFSH_OVraw;kc_nets_pol_" + year + "_4_freq_tnFVM_OVraw;kc_nets_pol_" + year + "_5_freq_tnNAT_OVraw;kc_nets_pol_" + year + "_6_freq_tnMET_OVraw;kc_nets_pol_" + year + "_7_freq_tnSMK_OVraw;kc_nets_pol_" + year + "_8_freq_tnEAT_OVraw;kc_nets_pol_" + year + "_9_freq_tnCON_OVraw;kc_nets_pol_" + year + "_10_freq_tnAFF_OVraw;kc_nets_pol_" + year + "_11_freq_tnPIZ_OVraw;kc_nets_pol_" + year + "_12_freq_tnBAK_OVraw;kc_nets_pol_" + year + "_13_freq_tnBNK_OVraw;kc_nets_pol_" + year + "_14_freq_tnCRD_OVraw;kc_nets_pol_" + year + "_15_freq_tnMUL_OVraw;kc_nets_pol_" + year + "_16_freq_tnLMPA_OVraw;kc_nets_pol_" + year + "_17_freq_tnVPA_OVraw;kc_nets_pol_" + year + "_18_freq_tnWARE_OVraw;kc_nets_pol_" + year + "_19_freq_tnDES_OVraw;kc_nets_pol_" + year + "_20_freq_tnURG_OVraw;kc_nets_pol_" + year + "_21_freq_tnHP_OVraw;kc_nets_pol_" + year + "_22_freq_tnRES_OVraw;kc_nets_pol_" + year + "_23_freq_tnRX_OVraw;kc_nets_pol_" + year + "_24_freq_tnMH_OVraw;kc_nets_pol_" + year + "_25_freq_tnDDS_OVraw", pr_path + "/tables/nets_intersects/kc_nets_" + year + "_biz_raw.txt", "false","true")

arcpy.Frequency_analysis("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/censusyear_list","W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/census_list","tractid","#")

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

arcpy.XToolsGP_Export2Text("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/censusyear_list","censusyear;tractid","W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/censusyear_list","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/censusyear_list.gdb/census_list",    "tractid",           "W:/GIS/Projects/king_county/data/processing/tables/censusyear_list/census_list.txt","false","false")