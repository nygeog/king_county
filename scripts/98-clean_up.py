import glob, os
filelist = glob.glob("W:/GIS/Projects/king_county/data/processing/tables/*.csv")
##print filelist
for f in filelist:
	os.remove(f)

filelist = glob.glob("W:/GIS/Projects/king_county/data/processing/tables/*.xml")
##print filelist
for f in filelist:
	os.remove(f)

filelist = glob.glob("W:/GIS/Projects/king_county/data/processing/tables/*.txt")
##print filelist
for f in filelist:
	os.remove(f)