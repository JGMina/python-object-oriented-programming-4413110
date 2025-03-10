# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: add methods for comparison and equality

# Challenge: use a magic method to make stocks and bonds sortable
# Stocks should sort from low to high on price
# Bonds should sort from low to high on yield

from abc import ABC, abstractmethod


class Asset(ABC):
    def __init__(self, price):
        self.price = price

    def __eq__(self, value):
        # if not isinstance(value, Asset):
        #     raise ValueError("Can't compare Asset and non-Asset")
        return (self.price == value.price)
    def __gt__(self, value):
        return (self.price == value.price)
    def __ge__(self, value):
        return (self.price == value.price)
    def __lt__(self, value):
        return (self.price == value.price)
    def __le__(self, value):
        return (self.price == value.price)




    @abstractmethod
    def __str__(self):
        pass


class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker
    
    def __str__(self):
        return f"ticker = {self.ticker}, price = {self.price}, company = {self.company}"

class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt
    
    def __str__(self):
        return f"price = {self.price}, description = {self.description}, duration = {self.duration}, yield amount = {self.yieldamt}"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]



# ------------------------------------------------
# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)
