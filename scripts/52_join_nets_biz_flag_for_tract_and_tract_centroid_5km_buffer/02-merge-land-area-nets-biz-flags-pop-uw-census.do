use "W:\GIS\Projects\king_county\data\output\_packages\52_join_nets_biz_flag_for_tract_and_tract_centroid_5km_buffer\working\censusyear_list.dta", clear
gen g_ct2000 = tractid
gen GEO_id2 = tractid
gen CTIDFP00 = g_ct2000
destring CTIDFP00, replace
merge m:1 CTIDFP00 using "W:\GIS\Projects\king_county\data\processing\tables\land_area\tracts_2000_land_water_area.dta"
drop _merge
merge m:1 g_ct2000 using "W:\GIS\Projects\king_county\data\processing\tables\land_area\tract_2000_land_area.dta"
drop _merge
merge m:1 g_ct2000 using "W:\GIS\Projects\king_county\data\processing\tables\land_area\tract_centroid_b5km_land_area.dta"
drop _merge
merge 1:1 censusyear using "W:\GIS\Projects\king_county\data\processing\tables\nets_year_flag_tables_stata\kc_nets_1990_2010.dta"
drop _merge
merge m:1 GEO_id2 using "W:\GIS\Projects\king_county\data\processing\tables\buffer_census_data\tract_2000_population.dta"
drop _merge
merge m:1 tractid using "W:\GIS\Projects\king_county\data\processing\tables\buffer_census_data\tract_2000_5km_buf_population.dta"
drop _merge frequency
merge m:1 g_ct2000 using "W:\GIS\Projects\king_county\data\processing\tables\census_uw_vars\kings_county_census_data.dta"
save "W:\GIS\Projects\king_county\data\output\_packages\52_join_nets_biz_flag_for_tract_and_tract_centroid_5km_buffer\king_county_tracts_2000_nets_biz_flags_tract_and_centroid_5km_buffer_1990_2010.dta", replace
