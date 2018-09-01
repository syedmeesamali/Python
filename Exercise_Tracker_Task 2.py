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
            data1 = list(csv.reader(csv_file))
            print(f'\t{row[0]} had {row[1]} ACTIVITY and did {row[2]} for {row[3]} mins, {row[4]} for')
            print(f'\t{row[5]} mins, {row[6]} for {row[7]} mins, {row[8]} for {row[9]} mins and {row[10]} for {row[11]} mins  ')
            line_count += 1
    print(f'Processed {line_count} lines.')
#End of import function

#    for i in range(len(data1)):
#        print(data1[i])

def update_Values():
    for i in range(len(data1)):
        print("Record # "+str(i)+": "+str(data1[i]))
    j=int(input("Please enter the record number you want to update or amend?"))
    print("Client ID is: "+str(data1[j][0]).upper())
    print("Exercize level is: "+str(data1[j][1]).upper())
    print("First activity is: "+str(data1[j][2]))
    print("For Duration of: "+str(data1[j][3]))
    print("Second activity is: "+str(data1[j][4]))
    print("For Duration of: "+str(data1[j][5]))
    print("Third activity is: "+str(data1[j][6]))
    print("For Duration of: "+str(data1[j][7]))
    print("Fourth activity is: "+str(data1[j][8]))
    print("For Duration of: "+str(data1[j][9]))
    print("Fifth activity is: "+str(data1[j][10]))
    print("For Duration of: "+str(data1[j][11]))
    k=int(input("Please enter the index of record to edit starting from 0 up to 11"))
    val_new=str(input("Please enter new value for existing value of: ["+str(data1[j][k])+"]"))
    data1[j][k]=val_new

    update_Values()

update_Values()
        
