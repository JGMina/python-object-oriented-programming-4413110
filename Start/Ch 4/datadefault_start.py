# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = 0.0          # those with no default value have to come first



@dataclass
class Book2:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory = price_func) # using field allows the use of functions to create the default value dynamically




b1 = Book()
b2 = Book2("War & Peace", "Leo Tolstoy", 1225)
b3 = Book2("The catcher in the rye", "JD Salinger", 234)


# ------------------------------------------------
# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------

print(b1)
print(b2)
print(b3)