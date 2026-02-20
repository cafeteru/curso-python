def hello():
    print("Hello, World!")


def hello_name(name: str):
    print(f"Hello, {name}!")


def hello_name_with_default(name: str = "World"):
    print(f"Hello, {name}!")


def add_two_numbers(a: int, b: int) -> int:
    return a + b


def hello_multiple_people(*names: str):
    for name in names:
        print(f"Hello, {name}!")


def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


def square(number: int) -> int:
    return number * number


hello()
hello_name("Alice")
hello_name_with_default()
result = add_two_numbers(3, 5)
print(f"The result of adding 3 and 5 is: {result}")
hello_multiple_people("Alice", "Bob", "Charlie")
people = ["Alice", "Bob", "Charlie", "David"]
hello_multiple_people(*people)
display_info(name="Alice", age=30, city="New York")
print(f"The square of 4 is: {square(4)}")
