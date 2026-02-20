# Example 1 : Defining and Instantiating a Class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} says {self.sound}"


# Creating an instance of Animal
dog = Animal(name="Dog", sound="Woof")
print(dog.make_sound())


# Example 2 : Inheritance
class Bird(Animal):
    def __init__(self, name, sound, can_fly):
        super().__init__(name, sound)
        self.can_fly = can_fly

    def fly(self) -> str:
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} cannot fly."


# Creating an instance of Bird
sparrow = Bird(name="Sparrow", sound="Chirp", can_fly=True)
print(f"{sparrow.make_sound()} and {sparrow.fly()}")


# Example 3: Class Method and Static Method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def from_square(cls, side_length):
        return cls(width=side_length, height=side_length)

    @staticmethod
    def is_square(width, height) -> bool:
        return width == height


# Creating instances of Rectangle
rectangle = Rectangle(width=10, height=20)
square = Rectangle.from_square(10)
print(rectangle.area())
print(square.area())

print(Rectangle.is_square(rectangle.width, rectangle.height))
print(Rectangle.is_square(square.width, square.height))

# Exercise
# Create a class Car with attributes make (the brand of the car)
# and year (the year the car was made). Include an instance method describe_car()
# that returns a string describing the car using these attributes.
# Also, add a static method is_vintage(year) that returns True if the car's year
# is more than 20 years from the current year, and False otherwise.
from datetime import datetime


class Car:
    def __init__(self, make: str, year: int):
        self.make = make
        self.year = year

    def describe_car(self):
        return f"This car is a {self.year} {self.make}."

    @staticmethod
    def is_vintage(year: int) -> bool:
        return datetime.now().year - year >= 20
