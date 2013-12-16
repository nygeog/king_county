import csv

W = "/Users/danielmsheehan/Dropbox"

pr_path = W + "/GIS/Projects/king_county/data/processing"
the_path = pr_path +"/tables/nets_year_flag_tables/_final/"

for year in range(1990,2011):
    with open(the_path + 'kc_nets_' + str(year) + '_final.txt','r') as csvinput:
        with open(the_path + 'kc_nets_' + str(year) + '_final_final.txt', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('year')
            all.append(row)

            for row in reader:
                row.append(str(year))
                all.append(row)

            writer.writerows(all)


for year in range(1990,2011):
    with open(the_path + 'kc_nets_' + str(year) + '_final_final.txt','r') as csvinput:
        with open(the_path + 'kc_nets_' + str(year) + '_final_final_final.txt', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('censusyear')
            all.append(row)

            for row in reader:
                row.append(row[0] + str(year))
                all.append(row)

            writer.writerows(all)