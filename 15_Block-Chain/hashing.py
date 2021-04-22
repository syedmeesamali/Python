from hashlib import sha256

#we know x =5 and (x*y) = ac23dc.........0 (ONE ZERO at END)
x = 7
y = 0 #we don't know value of y yet

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'The solution is y = {y}')
