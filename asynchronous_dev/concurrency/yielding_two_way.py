from collections import deque

friends = deque(('Rolf', 'Adam', 'Ashley'))

def get_friend():
    yield from friends # Allows you to yield from existing generators

def greet_friend(generated_friend):
    while True:
        try:
            friend = next(generated_friend)
            yield f'Hello {friend}!'
        except StopIteration:
            pass

friends_generators = get_friend()
greetings = greet_friend(friends_generators)
print(next(greetings))
print(next(greetings))