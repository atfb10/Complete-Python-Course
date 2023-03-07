friends = ['james', 'haigh', 'lars']

# show friend and position using a counter
counter = 0
for friend in friends:
    print(f'{counter}: {friend}')
    counter += 1

print('\n')

# show friend and position using enumeration
for counter, friend in enumerate(friends):
    print(f'{counter}: {friend}')

# Enumerate creates a list of tuples, where each value is a tuple of index and value
my_list = list(enumerate(friends))
print(my_list)