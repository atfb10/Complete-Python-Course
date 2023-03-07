# Magic of a class, is it can contain data & functions that act on the data

class Student:
    def __init__(self, name, grades):
        # Called a property inside a Class
        self.name = name
        self.grades = grades
    
    # Called Method inside a class
    def average(self):
        return sum(self.grades) / len(self.grades)

student1_grades = [80, 91, 92]
my_student = Student('adam', student1_grades)

print(my_student.average())


# How to change special methods in Python
# Every class should have a repr and str method
# Every class with a list object should have a len & getitem method
class Garage:
    def __init__(self):
        self.cars = []
    
    # Tells Python what to do when calling len method on an object of Garage class
    def __len__(self):
        return len(self.cars)
    
    # Be able to index cars property of a Garage object
    def __getitem__(self, i):
        return self.cars[i]

    # return string that represents object. Used for debugging
    def __repre__(self):
        return f'Garage {self.cars}'
    
    # string of car property of garage object
    def __str__(self):
        return f'Garage has {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford[0])

# Once you have defined the __len__ and __getitem__ methods, you can iterate over a property of a class
for car in ford:
    print(car)

print(ford)