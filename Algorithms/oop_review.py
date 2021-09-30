class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} old!")
    
#Pet in parenthesis means it will INHERIT properties of the Pet class
class cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} old and my color is {self.color}")

    def speak(self):
        print("Meooowwww")

class dog(Pet):
    def speak(self):
        print("Baaarkkk")

p = Pet("Tim", 25)
p.show()
c = cat("Bill", 34, "red")
c.show()
c.speak()