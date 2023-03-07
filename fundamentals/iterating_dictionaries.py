my_dictionary = {
    "brett": 23,
    "janice": 26,
    "bart": 29,
}

# Only keys
for name in my_dictionary:
    print(name)

# Only values
for age in my_dictionary.values():
    print(age)

# Get both
for name, age in my_dictionary.items():
    print(f'name = {name}. Age = {age}')