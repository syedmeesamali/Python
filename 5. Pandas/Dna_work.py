inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq.replace("\n","")
seq.replace("\r","")
