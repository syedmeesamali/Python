#csv library can be used to parse the csv files
import csv
with open('clientRecords.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} had {row[1]} ACTIVITY and did {row[2]} for {row[3]} mins, {row[4]} for')
            print(f'\t{row[5]} mins, {row[6]} for {row[7]} mins, {row[8]} for {row[9]} mins and {row[10]} for {row[11]} mins  ')
            line_count += 1
    print(f'Processed {line_count} lines.')
#End of import function
