friends = ['Rolf', 'Kevin', 'Reginald', 'Brant', 'Ryan', 'Clark']

# map take iterables and output iterable where each element has been altered by a function
# Arg 1 = function
# Arg 2 = iterable
lowered_friends = map(lambda names: names.lower(), friends) 
print(lowered_friends)

# Generator comprehension solution. This is the fastest performance wise
lowered_friends2 = (friend.lower() for friend in friends)
print(lowered_friends2)


# Another example
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])
    
user_list = [
    {'username': 'aforestier10', 'password': 'yum23'},
    {'username': 'aepratt03', 'password': 'heythere231'}
]

users = map(User.from_dict, user_list)