def greet():
    friend = yield
    print(f'hello, {friend}')

# g = greet()
# g.send(None) # Priming the generator
# g.send('Adam')

from collections import deque

friends = deque(('Rolf', 'Adam', 'Ashley'))

def friends_upper():
    while friends:
        upper_friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {upper_friend}')

def greet2(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet2(friends_upper())
greeter.send(None)
greeter.send('Hello')
print()
greeter.send('How are you')