class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

    # Allows you to iterate over a generator and perform built in functions such as len, sum, etc
    # For python, all you have to what is below
    def __iter__(self):
        return self
    

# Iterator: Used to get the next value
# Iterable: Used to go over all values of the iterator
    
for i in FirstHundredGenerator():
    print(i)

# How to create a generator on the fly
my_generator = (x for x in [1,2,3,4,5]) # Generator comprehension
print(next(my_generator))

# IMPORTANT: Different than list comprehension
my_list = [x * 2 for x in [1,2,3,4,5]]
print(my_list)