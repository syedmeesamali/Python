score = input("Enter Score: ")
try:
    sval = float(score)  
except:
    print("Some error! Exit!")
    quit()

if sval >= 0.9 and sval < 1.0:
    print("A")
elif sval >= 0.8:
    print("B")
elif sval >= 0.7:
    print("C")
elif sval >= 0.6:
    print("D")
elif sval > 0.0 and sval < 0.6:
    print("F")