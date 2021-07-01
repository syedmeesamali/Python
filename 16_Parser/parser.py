import os
import csv

inputfile = open('chat1.txt', errors='ignore')
outputfile = open('chat2.html', 'w')

message = """<html><head><title>SYED - Atef Chat</title>
<style>body { font-family: Arial, Helvetica, sans-serif; }</style></head><body>"""
outputfile.write(message)

for line in inputfile:
   val1 = line.split('[')
   if "<attached:" in str(val1[1]):
      val2 = str(val1[1]).replace("<attached: ", "<br><img src=\"../HTML/New folder/").replace(">", "\" /^><br>")
      outputfile.write(val2)
   else:
      outputfile.write("<h2>" + str(val1[1]) + "</h2>" + os.linesep)

#Close the html portion
outputfile.write("</body></html>")
