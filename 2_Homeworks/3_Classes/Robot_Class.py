class Robot:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am a robot with name " + self.name)
        else:
            print("Hi, I am a robot without name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == "__main__":
    x = Robot("Marvin")
