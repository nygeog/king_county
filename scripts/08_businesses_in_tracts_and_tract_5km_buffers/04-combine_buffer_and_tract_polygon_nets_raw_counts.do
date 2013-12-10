use W:\GIS\Projects\king_county\data\processing\tables\tract_pol_2000_nets_int_dis.dta 
gen g_ct2000 = CTIDFP00
gen netsrawcountbytractpoly = COUNT_CTIDFP00
label variable g_ct2000 "Census Tract 2000"
label variable netsrawcountbytractpoly "NETS business count by tract"
drop COUNT_CTIDFP00
merge 1:1 CTIDFP00 using "W:\GIS\Projects\king_county\data\processing\tables\tract_5km_2000_nets_int_dis.dta"
drop _merge
gen netsrawcountbytract5kmbuf = COUNT_CTIDFP00
label variable netsrawcountbytract5kmbuf "NETS business count by tract centroid 5 km buffer"
drop COUNT_CTIDFP00 CTIDFP00
replace netsrawcountbytractpoly  = 0 if (netsrawcountbytractpoly >= .)
replace netsrawcountbytract5kmbuf  = 0 if (netsrawcountbytract5kmbuf >= .)
save "W:\GIS\Projects\king_county\data\output\nets_intersects\tract_poly_and_5km_buffer_int_nets_raw.dta", replace
