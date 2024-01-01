# Create a Bus child class that inherits from the Vehicle class. The default fare
# charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we
# need to add an extra 10% on full fare as a maintenance charge. So total fare for
# bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self):
        self.capacity = 0

    def calculate_fare(self):
        return self.capacity * 100

class Bike(Vehicle):
    def __init__(self):
        self.capacity = 2
    
    def calculate_fare(self):
        return super().calculate_fare()

class Car(Vehicle):
    def __init__(self):
        self.capacity = 4
    
    def calculate_fare(self):
        return super().calculate_fare()

class Bus(Vehicle):
    def __init__(self,seats=50):
        self.capacity = seats

    def calculate_fare(self):
        base_fare = super().calculate_fare()  
        maintenance_charge = base_fare * 0.1  
        total_fare = base_fare + maintenance_charge
        return total_fare

def main():
    while True:
        print("1.Bike\n2.Car\n3.Bus\n4.Exit")
        a=int(input("Enter choice: "))
        if a==1:
            b=Bike()
            c=b.calculate_fare()
            print("Fare:",c)
        elif a==2:
            b=Car()
            c=b.calculate_fare()
            print("Fare:",c)
        elif a==3:
            d=int(input("Enter number of seats: "))
            b=Bus(d)
            c=b.calculate_fare()
            print("Fare:",c)
        elif a==4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()