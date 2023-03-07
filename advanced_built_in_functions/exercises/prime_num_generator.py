"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""
def prime_generator(bound):
    '''
    generator that takes argument bound as upper boundary and generates a prime number starting from 2 up to, but not including the upwards boundary
    ''' 
    for i in range(2, bound):
        for x in range(2, i):
            if i % x == 0:
                break
        else: yield i
        
g = prime_generator(20)
print(next(g))
print(next(g))
print(next(g))