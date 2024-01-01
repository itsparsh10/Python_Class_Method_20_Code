# Create three classes, “Person,” “Employee,” and “Student.” Use multiple
# inheritance to create a class “PersonInfo” that inherits from both “Employee” and
# “Student.” Add attributes and methods specific to each class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

    def work(self):
        print(f"{self.name} is working on a project")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

    def study(self):
        print(f"{self.name} is working on an assignment")


class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, department, student_id, major):
        Employee.__init__(self, employee_id, department)
        Student.__init__(self, student_id, major)
        Person.__init__(self, name, age)

    def display_person_info(self):
        self.display_employee_info()
        self.display_student_info()


def main():
    a=input("Enter your name: ")
    b=input("Enter your age: ")
    c=input("Enter employee ID: ")
    d=input("Enter your department: ")
    e=input("Enter student ID: ")
    f=input("Enter your major: ")
    person_info = PersonInfo(a,b,c,d,e,f)

    person_info.display_person_info()

    # Accessing methods from the Employee and Student classes
    person_info.work()
    person_info.study()

if __name__=="__main__":
    main()
