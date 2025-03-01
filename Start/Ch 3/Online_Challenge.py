# it was different from the one in the folder

# Python code​​​​​​‌‌​​‌‌​​‌‌​‌‌​​‌‌‌‌​‌‌‌​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = False

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # Put your comparison logic here.
    def __eq__(self, value):
    # if not isinstance(value, Asset):
    #     raise ValueError("Can't compare Asset and non-Asset")
        return (self.price == value.price)
    def __gt__(self, value):
        return (self.price > value.price)
    def __ge__(self, value):
        return (self.price >= value.price)
    def __lt__(self, value):
        return (self.price < value.price)
    def __le__(self, value):
        return (self.price <= value.price)



# ------------------------------------------------
# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------



# ~~~~~~~~~ TEST CODE ~~~~~~~~~
ticker1 = "XYZ"
ticker2 = "ABCD"
price1 = 100.0
price2 = 105.1
company1 = "XYZ Corporation"
company2 = "ABCD Company"

stock1 = Stock(ticker1, price1, company1)
stock2 = Stock(ticker2, price2, company2)

is_eq = (stock1 == stock2)
is_gt = (stock1 > stock2)
is_lt = (stock1 < stock2)
is_gte = (stock1 >= stock2)
is_lte = (stock1 <= stock2)

print(is_eq)
print(is_gt)
print(is_lt)
print(is_gte)
print(is_lte)