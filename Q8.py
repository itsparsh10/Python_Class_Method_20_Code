# Create a Python class called “Car” with attributes like make, model, and year.
# Then, create an object of the “Car” class and print its details.
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_details(self):
        print(f"Car: {self.make}\nModel: {self.model}\nYear: {self.year}")

def main():
    a=input("Enter make of car: ")
    b=input("Enter model: ")
    c=input("Enter year: ")
    d=Car(a,b,c)
    d.car_details()

if __name__ == "__main__":
    main()