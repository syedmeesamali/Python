import os
import csv

inputfile = open('chat1.txt', errors='ignore')
outputfile = open('chat2.html', 'w')

for line in inputfile:
   val1 = line.split('[')
   outputfile.write("<h4>" + str(val1[1]) + "</h4>" + os.linesep)
