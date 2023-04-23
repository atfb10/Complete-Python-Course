# Sets don't hold order. 
# Sets don't contain duplicate elements
friends = {"hans", "justin", "bella"}
yosemite_friends = {"ciaran", "bella", 'catherine'}

# Add friend
yosemite_friends.add("Nick")

# Remove friends
yosemite_friends.remove("Nick")

# Compare sets

# This gets who is in friends, but not yosemite friends
non_yosemite_friends = friends.difference(yosemite_friends) # No Bella
print(non_yosemite_friends)
print('\n')

# Gets who is NOT in both sets
not_in_both = friends.symmetric_difference(yosemite_friends) # Hans, Justin, Ciaran, Catherine
print(not_in_both)
print('\n')

# Gets who is in both sets
both_friends = friends.intersection(yosemite_friends) # Bella
print(both_friends)

# Create set of everyone, but will not make a duplicate (AKA only 1 bella)
all_friends = friends.union(yosemite_friends) # Hans, Justin, Bella, Ciaran, Catherine
print('\n')
print(all_friends)