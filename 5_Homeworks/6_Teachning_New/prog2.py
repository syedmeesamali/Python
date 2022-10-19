# Rate of interest
userInput = input("Principal: ")
P = float(userInput)

userInput = input("Please enter the interest rate: ")
r = float(userInput)

userInput = input("Please enter the years: ")
t = float(userInput)

# Calculate
total = P*(1+(r/100))**t

print("Final Amount to be paid: %8.2f" % total)