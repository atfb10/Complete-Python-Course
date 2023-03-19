import queue
from threading import Thread

# Atomic operation - one that cannot be interrupted. It must complete before removing the thread from the core

# NOTE: IMPORTANT - If you want to perform actions sequentially - You should not use threads
# However - If using threads and you want to perform actions sequentially - you must use queuing

counter = 0
job_queue = queue.Queue() # Things to be printed out
counter_queue = queue.Queue() # amounts by which to increase counter

def increment_manager() -> None:
    global counter
    while True:
        increment = counter_queue.get() # This waits until an item is available and then locks the queue. While a thread has this resource, no other thread can access this resource
        old_counter = counter
        counter = increment + old_counter
        job_queue.put((f'New counter value = {counter}', '-----------'))
        counter_queue.task_done() # This unlocks the queue

Thread(target=increment_manager(), daemon=True).start() # daemon = True, means the thread will run indefinetely

def printer_manager() -> None:
    while True:
        for obj in job_queue.get():
            print(obj)
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()