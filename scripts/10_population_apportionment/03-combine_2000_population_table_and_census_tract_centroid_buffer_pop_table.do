use W:\GIS\Projects\king_county\data\processing\tables\buffer_census_data\tract_2000_population.dta 
gen tractid = GEO_id2
merge 1:1 tractid using "W:\GIS\Projects\king_county\data\processing\tables\buffer_census_data\tract_2000_5km_buf_population.dta"
drop _merge
drop GEO_id2
gen g_ct2000 = tractid
drop tractid frequency
label variable pop2000 "Census Tract 2000 Population"
label variable g_ct2000 "Census Tract 2000 Census ID"
label variable pop2000trtcentroid5kmbuf "Census Tract 2000 Centroid with 5 km buffer population apportionment"
save "W:\GIS\Projects\king_county\data\output\population_tract_and_5km_centroid_buffer\population_tract_and_5k_centroid_buffer.dta", replace
