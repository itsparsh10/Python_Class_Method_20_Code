# Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Add
# methods and attributes specific to each subclass.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the furniture."

def main():
    dog_instance = Dog("Buddy", 3, "Golden Retriever")
    print(f"{dog_instance.name} is {dog_instance.age} years old and says: {dog_instance.make_sound()}")
    print(dog_instance.fetch())

    cat_instance = Cat("Whiskers", 2, "Gray")
    print(f"{cat_instance.name} is {cat_instance.age} years old and says: {cat_instance.make_sound()}")
    print(cat_instance.scratch())

if __name__=="__main__":
    main()