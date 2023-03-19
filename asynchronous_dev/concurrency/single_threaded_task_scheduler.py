def countdown(n):
    for i in range(n, 0, -1):
        yield i

tasks = [countdown(10), countdown(8), countdown(19)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        new_task = next(task)
        print(new_task)
        tasks.append(task)
    except StopIteration:
        print('task finished')