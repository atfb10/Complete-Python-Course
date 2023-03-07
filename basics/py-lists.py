friends = [
    'James',
    'Hans',
    'Justin',
    'Haigh'
]

for friend in friends:
    print(f'Name = {friend}')

first_friend_in_list = friends[0]
print(first_friend_in_list)

number_of_friends = len(friends)
print(number_of_friends)

friends_and_ages = [
    ["james", 24],
    ["hans", 26],
    ["Haigh", 26],
    ["justin", 25]
]

friend_3_age = friends_and_ages[2][1]
print(friend_3_age)

friends_and_ages.append(['Lars', 23])

num_friends = len(friends_and_ages)
new_friend = friends_and_ages[num_friends - 1]
print(new_friend)

# Convert list to string
comma_separated = ', '.join(friends)
print(f'My friends are {comma_separated}')