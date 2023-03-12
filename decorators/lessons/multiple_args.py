# How to have any number of arguments/parameters
# * is any number of different arguments/parameters
# ** is for dictionary arguments. The values are the value to the key in a dictionary object

def sum_all(*args) -> int:
    return sum(args)

numbers = [12, 100]
print(sum_all(12, 13, 100))

# Unpack a list
print(sum_all(*numbers))

def print_dictionary(**kwargs):
    for key, value in kwargs.items():
        print(f'key = {key}. value = {value}')

print_dictionary(name='Roxanne', id=1)

dict1 = {'name': 'Adam', 'id': 2, 'favorite color': 'Black'}

# Unpack a dictionary
print_dictionary(**dict1)