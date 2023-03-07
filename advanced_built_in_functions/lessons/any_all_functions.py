friends = [
    {
        'name': 'Adam',
        'location': 'Big Pine'
    },
    {
        'name': 'Haigh',
        'location': 'Seattle'
    },
    {
        'name': 'Carol',
        'location': 'Big Pine'
    }
]

# any - returns True if any element evaluates to True
your_location = input("put your location: ")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print('You have friends nearby!')

# all - returns True if all elements evaluate to True
if all(friends_nearby):
    print('Some of your friends are far away')