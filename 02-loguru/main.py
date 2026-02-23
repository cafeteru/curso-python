def hello():
    """Function that prints a greeting."""
    print("Hello, World!")


def hello_name(name: str):
    """Function that takes a name as an argument and prints a greeting."""
    print(f"Hello, {name}!")


def hello_name_with_default(name: str = "World"):
    """Function that prints a greeting with a default name."""
    print(f"Hello, {name}!")


def add_two_numbers(a: int, b: int) -> int:
    """Function that returns the sum of two numbers."""
    return a + b


def hello_multiple_people(*names: str):
    """Function that takes a variable number of names and prints a greeting for each."""
    for name in names:
        print(f"Hello, {name}!")


def display_info(**info):
    """Function that takes a variable number of keyword arguments and prints each key-value pair."""
    for key, value in info.items():
        print(f"{key}: {value}")


def square(number: int) -> int:
    """Function that returns the square of a number."""
    return number * number


hello()
hello_name("Alice")
hello_name_with_default()
RESULT = add_two_numbers(3, 5)
print(f"The result of adding 3 and 5 is: {RESULT}")
hello_multiple_people("Alice", "Bob", "Charlie")
people = ["Alice", "Bob", "Charlie", "David"]
hello_multiple_people(*people)
display_info(name="Alice", age=30, city="New York")
print(f"The square of 4 is: {square(4)}")
