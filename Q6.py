#Define a class attribute “color” with a default value white. i.e., Every Vehicle should be white.
class Vehicle:
    colour = 'white'
    def __init__(self,make):
        self.make = make
    def vehicle_info(self):
        print(f"Vehicle Info: {self.make} {self.colour}")

def main():
    a=Vehicle("BMW")
    a.vehicle_info()
    b=Vehicle("Audi")
    b.vehicle_info()
    c=Vehicle("Nissan")
    c.vehicle_info()

if __name__ == '__main__':
    main()