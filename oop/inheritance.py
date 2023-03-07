class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

# Child class of working student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # This is how you inherit properties from parent class
        self.salary = salary

    # Method(s) in parent is included automatically

    # New child method
    def weekly_salary(self): return self.salary * 40

test_working_student = WorkingStudent('jeff', 'mit', 15.25)
grades = [80, 95, 100]
test_working_student.grades.extend(grades)
print(test_working_student.average())
print(test_working_student.weekly_salary())