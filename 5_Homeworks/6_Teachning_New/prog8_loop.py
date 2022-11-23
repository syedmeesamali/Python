rate = 7.5
initial_balance = 11000
target = 2 * initial_balance

#Initialize the variables
balance = initial_balance
year = 0

while balance < target:
    year += 1
    interest = balance * (rate / 100)
    balance = balance + interest

print("Total amount was doubled in {} years!".format(year))