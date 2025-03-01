# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "class B"
        self.which = "class B which"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.prop1, self.prop2, self.name, self.which)

# Always clear the Terminal before new execution
import os
os.system('cls' if os.name == 'nt' else 'clear')

c = C()
print(C.__mro__)        # returns the orders of classes down to objects
c.showProps()