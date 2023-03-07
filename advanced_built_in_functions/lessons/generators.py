# Generator - Function that remembers the state its in between executions

# Example
# Yield gives the value, and then remembers that is where it is at for the next time the function is called
# Very useful for having a function stop running temporarily, and then having it run again when ready
# ^ Crucial for asynchronous programming
def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1

# Show how it is used
g = hundred_numbers()
print(next(g)) # This will print 0
print(next(g)) # This will print 1
print(next(g)) # This will print 2

# This creates a list from generator. Will print 0-99
print(list(g))