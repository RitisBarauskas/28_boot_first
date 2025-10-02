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


def greet(count=1):
    for _ in range(count):
        name = get_random_name()
        print(f"Hello, {name}!")
