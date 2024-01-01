#WAP to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        dob_date = datetime.strptime(self.dob, '%Y-%m-%d')
        current_date_time = datetime.now()
        age = current_date_time.year - dob_date.year - ((current_date_time.month, current_date_time.day) < (dob_date.month, dob_date.day))
        return age

    def displayinfo(self):
        print(f"Your Name is : {self.name}")
        print(f"Your Country Is : {self.country}")
        print(f"Your Dob Is : {self.dob}")
        print(f"Your Current Age Is : {self.calculate_age()} Years ")

name_input = input("Enter Your Name: ")
country_input = input("Enter Your Country Name: ")
dob_input = input("Enter The Dob (YYYY-MM-DD): ")

person = Person(name_input, country_input, dob_input)
person.displayinfo()
