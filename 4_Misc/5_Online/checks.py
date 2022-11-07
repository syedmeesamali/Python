def func1():
    i = 10
    while i > 0:
        print("This is loop # {}: ".format(i))
        i = i - 1

def main():
    func1()

main()

x = ['ab', 'cd']
#print(list(map(lambda x: len(x), x)))

a = [1, 2, 3]
b = [2, 1, 3]
#print(a == b)
#print(set(a) == set(b))

f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i > 2:
            break
#print(f.closed)

az = 'abcd'
for i in range(len(az)):
    az[i].upper()
#print(az)

a = [1, 2, 3, 4, 5]
a.pop()
print(a)
a.pop(2)
print(a)

inp = ['a', 'b', 'c']
print(inp)

for i in inp:
    inp.append(i.upper())
print(inp)

t = '%(a)s %(b)s %(c)s'
print(t % dict(a = 'Welcome', b = 'to', c='Turing'))

def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)

class Welcome:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Welcome to ", self.name)

cw = Welcome('Turing')
cw.say_hello()

def add(c, k):
    c.test = c.test + 1
    k = k + 1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0
    for i in range(0, 25):
        add(p, index)
    print("p.test", p.test)
    print("idx", index)

main()

class Hello:
    def __init__(self, a='Welcome to '):
        self.a = a

    def welcome(self, x):
        print(self.a + x)

h = Hello()
h.welcome('Turing')

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
#print(z)

inp = ['a', 'b', 'c', 'd']
inp.insert(3, 'z')
print(inp)

inp = [2, 5J, 6]
inp.sort()
print(inp)

a = [1, 2, 3, 4, 5]
m = map(lambda x: 2**x, a)
print(list(m))

b = [1, 2, 3, 4]
c = [sum(b[0:x+1]) for x in range(0, len(b))]
print(c)

try:
    print("Hello")
except:
    print("An exception")
finally:
    print("World")

print([i.lower() for in in 'TURING'])

i = 'welcome'
def welcome(i):
    i = i + ', Welcome to turing'
    return i

welcome('Developer')
print(i)