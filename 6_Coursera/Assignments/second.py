hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter rate:"))
if h > 40:
    extra_hours = h - 40
pay = 40 * rate + extra_hours * rate * 1.5
print(pay)