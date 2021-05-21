import os

with open("all.html", "w") as a:
    for path, subdirs, files in os.walk(r'C:\Users\SYED\Downloads\New folder'):
       for filename in files:
         f = os.path.join(path, filename)
         a.write("<img src=\"" + str(f) + "\" /^>" + os.linesep) 
