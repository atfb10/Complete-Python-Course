# Generator class
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    
    def __next__(self):
        if self.number < 100:
            current = self.number + 1
            self.number += 1
            return current
        else:
            raise StopIteration('Number is 100 or greater')
        
# object of my first hundred generator
my_generator_object = FirstHundredGenerator()
print(my_generator_object.number)
print(next(my_generator_object))

