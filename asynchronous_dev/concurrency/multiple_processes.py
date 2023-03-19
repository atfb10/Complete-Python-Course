import time
from concurrent.futures import ProcessPoolExecutor

# Slow function. Big maths
def complex_computation():
    start = time.time()
    print('starting calculating')
    [x**2 for x in range(20000000)]
    print(f'time for complex_calculation to run = {round(time.time() - start, 2)} seconds')

def complex_computation2():
    start = time.time()
    print('starting calculating')
    [x**3 for x in range(2000000)]
    print(f'time for complex_calculation2 to run = {round(time.time() - start, 2)} seconds')

# NOTE: Multiprocessing
if __name__ == "__main__":
    '''
    in windows OS - all multiprocessing must be performed within if __name__ == "main":
    '''
    with ProcessPoolExecutor(max_workers=2) as process_pool:
        process_pool.submit(complex_computation)
        process_pool.submit(complex_computation2)