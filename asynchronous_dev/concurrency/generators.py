def countdown(n):
    for i in range(n, 0, -1):
        yield i
    return

def while_countdown(n):
    while n > 0:
        yield n
        n -= 1
    return

my_countdown = countdown(12)
my_countdown2 = while_countdown(20)
print(next(my_countdown))
print(next(my_countdown2))
print(next(my_countdown))
print(next(my_countdown2))