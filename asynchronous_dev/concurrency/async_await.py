from collections import deque
from types import coroutine

friends = deque(('Ashley', 'Haigh', 'Justin', 'Hans'))

@coroutine
def friends_to_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

async def greet(greeting_data):
    await greeting_data

greeter = greet(friends_to_upper())
greeter.send(None) # Priming the generator
greeter.send('Hello')
print()
greeter.send('How are you')
