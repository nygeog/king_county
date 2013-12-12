King County NETS
===========
This project takes place in King County, Washington. The data involved is cardiovascular outcome data (which I don't have access to) and NETS business data (what is the time frame? range? Could reference NETS data years).

Set is 378091, only 378086 within valid xy bounds of UTM NAD83 Zone 10N (meters)
Then 377363 in the county of King County


Tasks
=====

1. Gina would like the population and land area and business counts for all King County census tracts, not just the ones UW provided data on

tractid, population, land_area, business counts, 5kmbufpop, 5km land area 5km business counts



2. Instead of ZCTA for King County, Gina is interested in characterizing a 5km buffer from the census tract centroid.



using the 2000 boundaries, for each of the 21 years. 1990-2010. raw is uncollasped, + collapsed. 

Do I have a variable called Census year, census tract followed by year. 


so format the data longways

so each census tract

unique id 


tract (11 dig) + year (1990-2010)


tractid + 1990
			1991
			1992
			1993


Use 

Do for all 25 business types

25 column for counts each biz type

Needs 7833 rows

OV extension on biz field is raw
OV_col is the collapsed




just use the Stata Labels, not data diciotnary. 


gen newfield 


for nyc use 2010, same exercise for John Logan's data. 

KingCountyONLY_qr_count_raw&collapsed.dta (file want it to look like)

tn = number (count) tract number

bn = buffer number 


finestflag_OV is what we are interested in.

a frequency on BEH_ID;finestflag_OV

<!---
Scripts
=======

The following are the list of folders with scripts for this project:

00_dir_struct

01_tanya_stata_code

02_input

03_spatial_join

04_prior_constructed_census_vars

05_census_data_esri_pop_land_water_area

06_add_projected_xy_and_uid_for_round_10m_xy

07_buffers

99-clean_up.py

XX_join_tables_stata
-->

end. 
