import arcpy

arcpy.CreateFileGDB_management("C:/Users/DanielMSheehan/Desktop/king_county/data/processing","king_county","CURRENT")
arcpy.CreateFileGDB_management("C:/Users/DanielMSheehan/Desktop/king_county/data/processing","intersects", "CURRENT")