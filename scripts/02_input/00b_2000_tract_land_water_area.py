import arcpy

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "tracts_2000"
arcpy.Select_analysis("tracts_2000","V:/Dropbox/GIS/Projects/king_county/data/input/census.gdb/tracts_2000_king_county",""""STATEFP00" = '53' AND "COUNTYFP00" = '033'""")