friends = ['james', 'haigh', 'lars']
ages = [25, 26, 23]

# Zip function will combine two lists into a list of tuple objects
# It will look like this: var = [('james', 25), ('haigh', 26), ('lars', 23)]
list_of_tups = zip(friends, ages)

# Then can turn into a dictionary
my_dict = dict(list_of_tups)

# Shorter
my_dict = dict(zip(friends, ages))