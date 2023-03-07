numbers = [0, 1, 2, 3, 4]

# List comprehension
doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers)

# Very powerful!
ages = [23, 21, 42, 63]
friend_ages = [f'my friend is {age} years old!' for age in ages]

for msg in friend_ages:
    print(msg)

# turn all names to lower case using list comprehension
friends = ['Hans', 'Haigh', 'Justin']

lowercase_names = [name.lower() for name in friends]
print(lowercase_names)

# List comprehensions with conditionals
odd_ages = [age for age in ages if age % 2 == 1]
print(odd_ages)

# Lets make a list of who is in both, using list comprehensin
friends = ['Hans', 'Haigh', 'Justin']
new_friends = ['bella', 'Haigh', 'Justin']

overlap = [
    name for name in friends if name in new_friends
]

print(overlap)