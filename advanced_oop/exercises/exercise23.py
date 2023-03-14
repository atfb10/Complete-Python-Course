"""
Define your Salary class and Promotable class so that the Employee class objects may work like this:
rolf = Employee(15.0)
print(rolf.weekly_salary())     # --> prints out rolf's weekly salary (15.0 * 40 = 600.0)
rolf.promote(5.0)       # rolf's hourly salary (rate) increases by 5.0 (15.0 + 5.0 = 20.0)
print(rolf.weekly_salary())     # --> prints 800.0  (20.0 * 40 = 800.0)
"""


class Salary:
    def calculate(self, hours: float) -> float:
        return self.rate * hours


class Promotable:
    def promote(self, hourly_increase: float):
         self.rate += hourly_increase

# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float) -> None:
        self.rate = rate
        return

    def weekly_salary(self) -> float:
        return self.calculate(40)