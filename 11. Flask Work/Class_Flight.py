class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight Origin: {self.origin}")
        print(f"Flight Destination: {self.destination}")
        print(f"Flight Duration: {self.duration}")

    def delay(self, amount):
        self.duration += amount

def main():
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()
    f1.delay(25)
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=140)
    f2.print_info()
    f2.delay(10)
    f2.print_info()

if __name__ == "__main__":
    main()
