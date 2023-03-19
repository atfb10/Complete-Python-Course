import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# Slow function. It is slow, because it is waiting for a user to type. User typing is slow
def ask_user():
    start = time.time()
    user_input = input('Enter your name: ') # Blocking operation - this is what makes this thread slow
    greeting = f'Hello {user_input}'
    print(greeting)
    print(f'time for ask_user to run = {round(time.time() - start, 2)} seconds')

# Slow function. Big maths
def complex_computation():
    start = time.time()
    print('starting calculating')
    [x**2 for x in range(20000000)]
    print(f'time for complex_calculation to run = {round(time.time() - start, 2)} seconds')

program_start_time = time.time()
ask_user()
complex_computation()

# NOTE: This will take the amount of time for both functions to run
print(f'Single thread time for program to run = {round(time.time() - program_start_time, 2)} seconds\n')

# NOTE: THREADING
thread_start_time = time.time()
thread1 = Thread(target=complex_computation)
thread2 = Thread(target=ask_user)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# NOTE: IMPORTANT - It takes about as long as the longest running function
print(f'2 thread time with Threading to run = {round(time.time() - thread_start_time, 2)} seconds')


# NOTE: THREADING - Simplified using ThreadPoolExecutor. This is much much
thread_start_time = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    '''
    creates pool of threads
    with statement ensures that all threads completely execute prior to moving on in program
    '''
    pool.submit(ask_user)
    pool.submit(complex_computation)

print(f'2 thread time with ThreadPoolExecutor to run = {round(time.time() - thread_start_time, 2)} seconds')

# NOTE: Do not use multiple threads for multiple CPU intensive functions! it will just pass the thread in and out of the process... 
# AKA its slower - use multiprocessing in this scenario