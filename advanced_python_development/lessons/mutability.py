# Mutable data is data that can be changed once created
# Immutable data is data that cannot be changed once created

# immutable data types in Python: int, floats, strings, tuples
# All  functions return new objects for immutable data types

# IMPORTANT: It is a bad idea to make default arguments for Python functions with mutable data types.
# ONLY make default arguments for types: int, float, str, tuples
# Using mutable default arguments leads to horrible data issues. Has to do with pointers


friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Roger': 41
}

# id(variable) gives the location of the variable stored in memory
location_in_memory = id(friends_last_seen)
print(location_in_memory)

# __iadd__ implementations do work on self. __add__() implementation creates new variable. Example below
l = [2,5, 1]

# This is the same object
print(id(l))
l += [8, 0] # This is an iadd implementation. Modification is done the l object it self
print(id(l))

# This creates a new object
l = l + [3, 1] # This is an add implementation. 
print(l)