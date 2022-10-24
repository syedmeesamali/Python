import datetime as dt

names = ['ali', 'zara', 'jen', 'john', 'ray']
ages = [33, 25, 30, 37, 40]

datelist = []
datelist.append(dt.date(1985, 10, 1))
datelist.append(dt.date(1995, 6, 2))
datelist.append(dt.date(1990, 7, 15))
datelist.append(dt.date(1984, 8, 5))
datelist.append(dt.date(1982, 11, 7))

#print(names)
print()

#print(ages)
print()

dateval = []

#datelist.sort(reverse=True)
for date1 in datelist:
    #print(f"{date1: %Y - %m - %d}")
    dateval.append(str(date1.year) + '_' + str(date1.month) + '_' + str(date1.day))

combined = zip(names, ages, dateval)
for item in combined:
    print(item)
print()