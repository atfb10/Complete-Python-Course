# 3 types of methods
# 1. Instance method: performs action on object of class. Parameter passed in is self
# 2. @classmethod: performs an action on the class itslef. Takes cls as the paramete
# 3. @staticmethod: Takes no parameters, but performs an action.
# Generally - never use static method. Only use good ole' fashioned instance methods or @classmethods. @staticmethods are similar to class methods, but with less functionality. 
# ALWAYS use @classmethod if the method does not take self & the class is getting inherited from 
# ONLY use @staticmethod if it is in a class that never gets inherited from

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    # Instance method Example
    def avg(self): return sum(self.grades) / len(self.grades)

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>' # .2f prints to two decimal places

    # Creates a new FixedFloat object by adding two objects together. 
    # Allows you to do it by calling the Class
    # When this method is called, it keeps the class correct; whether it is an object of this class, or any of its Child classes
    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)

# @classmethod example use exmaple
number = FixedFloat.from_sum(23.11, 82.22)
print(number)

class EuroFixedFloat(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'E'
    
    def __repr__(self):
        return f'{self.symbol}{self.amount:.2f}'

    # static method example
    @staticmethod
    def say_gibberish():
        print("The euro is the superior currency")


my_euro = EuroFixedFloat(23.22)

# @staticmethod example
my_euro.say_gibberish()