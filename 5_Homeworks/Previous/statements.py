#Below program will print result when the bear is friendly even if we extend the dictionary
bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear]=="friendly":
        print("Hello, "+bear+" bear!")
    else:
        print("odd")

#to check primeness of a number
is_prime = True
n=19
for i in range(2,n):
   if n%i == 0:
     is_prime = False
print(is_prime)


n=100
number_of_times = 0
while n >= 1:
   #below is division with truncation of decimal part
   n //= 2
   number_of_times += 1
print(number_of_times)

filename="input.txt"
for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

F = open("output.txt","w")
for i in range(10):
    F.write(str(i)+"\n")
F.close()
