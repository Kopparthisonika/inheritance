# Task 1: Basic Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    pass


s = Student("Ravi", 20)
s.display_person()


# Task 2: Inherited & Specific Methods

class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()
d.eat()
d.sleep()
d.bark()

# Inherited methods: eat(), sleep()
# Specific method: bark()


# Task 3: Method Overriding

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car is starting with a key")


c = Car()
c.start()

# Overridden method: start()