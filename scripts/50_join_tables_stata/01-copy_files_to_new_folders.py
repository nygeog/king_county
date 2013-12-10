import shutil, os

folder_path = "W:/GIS/Projects/king_county/data/processing/tables"

list_of_files = [
"tracts_2000_esri_pop.dta",
"tracts_2000_us_census.dta",
"ct1990.dta",
"ct2000.dta",
"ct2010.dta",
"zt2000.dta",
"zt2010.dta",
"kings_county_census_data.dta",
"tract_2000_land_area.dta",
"tract_centroid_b5km_land_area.dta",
"tracts_2000_land_water_area.dta",
"tract_5km_2000_nets_int_dis.dta",
"tract_pol_2000_nets_int_dis.dta",
"tract_poly_and_5km_buffer_int_nets_raw.dta",
"utm_xy_round.dta"
]

list_of_folders = [
"census_data",
"census_data",
"census_geographies",
"census_geographies",
"census_geographies",
"census_geographies",
"census_geographies",
"census_uw_vars",
"land_area",
"land_area",
"land_area",
"nets_intersects",
"nets_intersects",
"nets_intersects",
"utm_xy_round"
]

for listoffiles, listoffolders in zip(list_of_files, list_of_folders):
	shutil.copy2(folder_path + "/" + listoffiles, folder_path + "/" + listoffolders + "/" + listoffiles)
	os.remove(folder_path + "/" + listoffiles)