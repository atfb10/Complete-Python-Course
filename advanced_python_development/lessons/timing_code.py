import time

powers = lambda limit: [x**2 for x in range(limit)]

# Time how long something takes
start = time.time()
powers(5000000)
end = time.time()

# function to time the amount of time between starting running a function and its completion
def time_me(func):
    start = time.time()
    func()
    end = time.time()
    return f'{end-start} seconds'

powers_time_elapsed = time_me(lambda: powers(5000000))
print(powers_time_elapsed)