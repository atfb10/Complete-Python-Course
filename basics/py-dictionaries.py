# Allows to store keys and values
# Cannot have duplicate keys. Can have duplicate values
# Order is kept

friend_ages = {
    'rolf': 24,
    'kevin': 21,
    'lars': 23,
    'jeff': 58
}

# Get age by key
rolf_age = friend_ages['rolf']

# add to dictionary
friend_ages['carol'] = 30

# Update by key
friend_ages['rolf'] = 25

# Have list with multiple pieces of information about an individual
friends = [
    {"name": "hans", "age":26},
    {"name": "tim", "age":27},
    {"name": "haigh", "age":26},
]

# Get first friends name
first_friend_name = friends[0]['name']
print(first_friend_name)

# Get third friends age
third_age = friends[2]['age']
print(third_age)

# Get second all information of second friend
second_friend = friends[1]