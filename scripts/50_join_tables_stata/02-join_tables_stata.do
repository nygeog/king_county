use W:\GIS\Projects\king_county\data\input\kco_regeocode_bygooglemap\kco_regeocode_bygooglemap_TK.dta 
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\ct1990.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\ct2000.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\ct2010.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\zt2000.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\zt2010.dta"
drop _merge
merge m:1 g_ct2000 using "W:\GIS\Projects\king_county\data\processing\tables\kings_county_census_data.dta"
drop _merge
merge m:1 BEH_ID using "W:\GIS\Projects\king_county\data\processing\tables\utm_xy_round.dta"
drop _merge

save "W:\GIS\Projects\king_county\data\output\kings_county_census.dta", replace
