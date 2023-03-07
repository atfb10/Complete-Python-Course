# Allows one to call method like a property
# Only do this, when method is just returning a value, calculated from an objects properties themselves

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    # Allows one to call method like a property
    # Only do this, when method is just returning a value that is calculated from an object's properties themselves
    @property
    def average(self): return sum(self.grades) / len(self.grades)

    # Another example
    @property
    def is_dumb(self): 
        if self.average < 75: return True
        return False


# Create a student object
grades = [100, 100, 85]
test_student = Student('jeff', 'mit')
test_student.grades.extend(grades)

# Use case example. Calls average like a property instead of like a method
print(test_student.average)
print(test_student.is_dumb)
