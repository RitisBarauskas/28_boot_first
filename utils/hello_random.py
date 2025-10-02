import random


NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Eve",
]


def get_random_name():
    return random.choice(NAMES)


def greet():
    name = get_random_name()
    print(f"Hello, {name}!")
