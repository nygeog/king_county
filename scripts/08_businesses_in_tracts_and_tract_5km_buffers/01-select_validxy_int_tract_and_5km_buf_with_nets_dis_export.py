arcpy.Select_analysis("W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts","W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts_valid_xy","POINT_X > 0 AND POINT_Y > 0 ")
arcpy.Select_analysis("W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts","W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts_2000","BEH_2000 = 1")

arcpy.Intersect_analysis("W:/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000 #;W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts_2000 #","W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_pol_2000_nets_int","ALL","#","INPUT")
arcpy.Intersect_analysis("W:/GIS/Projects/king_county/data/processing/census_tract_centroid_buffers.gdb/utm_z10n/tracts_2000_centroid_5km_buf #;W:/GIS/Projects/king_county/data/processing/king_county.gdb/king_county_pts_2000 #","W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_5km_2000_nets_int","ALL","#","INPUT")

arcpy.Dissolve_management("W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_5km_2000_nets_int","W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_5km_2000_nets_int_dis","CTIDFP00","CTIDFP00 COUNT","MULTI_PART","DISSOLVE_LINES")
arcpy.Dissolve_management("W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_pol_2000_nets_int","W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_pol_2000_nets_int_dis","CTIDFP00","CTIDFP00 COUNT","MULTI_PART","DISSOLVE_LINES")

arcpy.XToolsGP_Export2Text("W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_5km_2000_nets_int_dis","CTIDFP00;COUNT_CTIDFP00","W:/GIS/Projects/king_county/data/processing/tables/tract_5km_2000_nets_int_dis.txt","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/king_county/data/processing/nets_tract_intersects.gdb/utm_z10n/tract_pol_2000_nets_int_dis","CTIDFP00;COUNT_CTIDFP00","W:/GIS/Projects/king_county/data/processing/tables/tract_pol_2000_nets_int_dis.txt","false","false")

