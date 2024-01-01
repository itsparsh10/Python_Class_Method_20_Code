# Create a base class called “Vehicle” with a method called “drive.” Implement two
# subclasses, “Car” and “Bicycle,” that inherit from “Vehicle” and override the “drive”
# method with their own implementations.
class Vehicle:
    def drive(self):
        print("Vehicle is being driven")
    
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle is being driven")

def main():
    vehicle=Vehicle()
    car=Car()
    bicycle=Bicycle()

    vehicle.drive()
    car.drive()
    bicycle.drive()

if __name__ == "__main__":
    main()