# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int      # not enforced
    price: float

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price

    def bookinfo(self):
        return f"{self.title} by {self.author}, has {self.pages} pages and costs {self.price}"


# ------------------------------------------------
# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------




# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)
print(b1.bookinfo())

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b2)
print(b1 == b3)

# TODO: change some fields
b1.pages = 50000
print(b1)
print(b1 == b2)
print(b1 == b3)