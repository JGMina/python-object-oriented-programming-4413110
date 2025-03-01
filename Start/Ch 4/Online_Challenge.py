# it was different from the one in the folder

# Python code​​​​​​‌‌​​‌‌​​‌‌​‌‌​​‌‌‌‌​‌‌‌​​ below
# Use print("messages...") to debug your solution.


show_expected_result = False
show_hints = False

from dataclasses import dataclass

# @dataclass (eq = False)     Necessary in older version of Python as the dataclass generate an inherent __eq__
@dataclass
class Asset:
    price: float

    def __eq__(self, value):
        return (self.price == value.price)
    def __gt__(self, value):
        return (self.price > value.price)
    def __ge__(self, value):
        return (self.price >= value.price)
    def __lt__(self, value):
        return (self.price < value.price)
    def __le__(self, value):
        return (self.price <= value.price)

@dataclass
class Stock(Asset):
    ticker: str
    company: str

@dataclass
class Bond(Asset):
    description: str
    duration: int
    interest: float




# ------------------------------------------------
# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------



# ~~~~~~~~~ TEST CODE ~~~~~~~~~
ticker = "ABCD"
price = 200.00
description = "ABCD Corporation"

bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Stock(price, ticker, description)
bond = Bond(bondprice, bondname, duration, interest)

print(stock == bond)
print(stock > bond)
print(stock < bond)
print(stock >= bond)
print(stock <= bond)