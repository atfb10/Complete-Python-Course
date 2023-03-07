class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop # stop defines the range (exclusive upper bound) in which we search for the primes
        self.number = 2

    def __next__(self):
        limit = self.stop
        for i in range(self.number, limit):
            for x in range(2, i):
                if i % x == 0:
                    self.number += 1
                    break
            else:
                self.number += 1
                return i

# Create the object
my_generator_object = PrimeGenerator(100)

# Ensure the starting number is 2
print(f'Generator Number: {my_generator_object.number}')

# Call next, see that the first prime number is 2
print(next(my_generator_object))

# Ensure the number has incremented by 1
print(f'Generator Number: {my_generator_object.number}')

# Ensure the next 2 numbers are 3 and 5
print(next(my_generator_object)) 
print(next(my_generator_object)) 