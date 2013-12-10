use W:\GIS\Projects\king_county\data\output\nets_intersects\tract_poly_and_5km_buffer_int_nets_raw.dta 
merge 1:1 g_ct2000 using "W:\GIS\Projects\king_county\data\output\land_area\tract_2000_land_area_and_buf_5km_land_area.dta"
drop _merge
merge 1:1 g_ct2000 using "W:\GIS\Projects\king_county\data\output\population_tract_and_5km_centroid_buffer\population_tract_and_5k_centroid_buffer.dta"
drop _merge
save "W:\GIS\Projects\king_county\data\output\_packages\tract_and_centroid_5km_buffer_land_area_nets_businesses_population\tract_and_centroid_5km_buffer_land_area_nets_businesses_population.dta"
