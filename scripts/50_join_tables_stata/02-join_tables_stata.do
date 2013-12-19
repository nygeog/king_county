use "W:\GIS\Projects\king_county\data\input\nets_from_tanya_20131211\KingCounty_finalxy_flag.dta", clear 
drop  unique_xy_round g_ct1990 g_ct2000 g_ct2010 g_zt2000 g_zt2010 g_2000state g_2000county


merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\census_geographies\ct1990.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\census_geographies\ct2000.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\census_geographies\ct2010.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\census_geographies\zt2000.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\census_geographies\zt2010.dta"
drop _merge
merge m:1 g_ct2000 using "W:\GIS\Projects\king_county\data\processing\tables\census_uw_vars\kings_county_census_data.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\utm_xy_round\utm_xy_round.dta"
drop _merge

save "W:\GIS\Projects\king_county\data\output\kings_county_census.dta", replace
