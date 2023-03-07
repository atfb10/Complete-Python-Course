# Get friends who's name starts w/ letter 'R'
friends = ['Rolf', 'Kevin', 'Reginald', 'Brant', 'Ryan', 'Clark']
def starts_with_r(friend) -> bool:
    return friend.startswith('R')

# Get all items in list that start with 'R' by using the filter()
# arg 1: function that returns true or false
# arg 2: iterable
# It is a generator
friends_start_r = filter(starts_with_r, friends)

print(next(friends_start_r))
print(next(friends_start_r))

# Use filter by passing in a lambda as first argument
friends_end_n = filter(lambda friend: friend.endswith('n'), friends)
print(next(friends_end_n))
print(next(friends_end_n))

# filter is the same as generator comprehension. This is the fastest performance wise
friends_with_k = (friend for friend in friends if 'k' in friend.lower())
print(next(friends_with_k))