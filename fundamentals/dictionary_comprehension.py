# example of dictionary comprehension
friends = ['james', 'haigh', 'lars']
ages = [25, 26, 23]

friend_info = {
    friends[friend]: ages[friend] for friend in range(len(friends))
}

print(friend_info)

# Much better to use zip function. see zip.py