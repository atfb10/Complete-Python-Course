# queue - first in first out
# stack - last in first out

from collections import Counter, defaultdict, deque, namedtuple ,OrderedDict
'''
* counter 
* defaultdict
* ordereddict
* namedtuple
* deque
'''

device_temperatures = [13.5, 23.4, 13.5, 81.5, 54.12, 13.5]
# Counter example. Create a counter object. Then access values like a dictionary
temperature_counters = Counter(device_temperatures)
thirteen_five_count = temperature_counters[13.5]
print(thirteen_five_count)

coworkers = [
    ('Rolf', 'MIT'),
    ('Kevin', 'Georgia Tech'),
    ('Rolf', 'Cambridge'),
    ('Ann', 'Dartmouth')
]

# defaultdict. Keeps each key unique, but allows to have multiple values per key!
# The function you pass as an argument to defaultdict() puts that value in that data type. Example below, 1 key, but list of values per key
alma_mater = defaultdict(list)
# set its default value
alma_mater.default_factory = None
for coworker, university in coworkers:
    alma_mater[coworker].append(university)
print(alma_mater['Rolf'])
print(alma_mater['Ann'])

# OrderedDict keeps the order of insertation. NOTE: As of python 3.7, dictionaries keep their order any way
od = OrderedDict()
od['Rolf'] = 3
od['Bart'] = 9
od['Jan'] = 2
# move_to_end() moves key to end
od.move_to_end('Bart')
# move_to_end(arg, last=False) moves key to start
od.move_to_end('Jan', last=False)
# pop_item removes last item in dictionary
od.popitem()
for key, value in od.items():
    print(f'{key}: {value}')

# namedtuple - like a tuple but each element has a name. and the tuple itself has a name
# Initialize the constructor with the first argument being the variable name. 
# The second, being the name of you would like each index of the tuple to be 
Account = namedtuple('Account', ['name', 'balance'])
# Create an account
account = Account('Checking', 1850)
# Now can access by name...
print(f'Your {account.name} account\'s balance is ${account.balance}')

# A deque or double ended queue is a queue in which you can add or remove items on either end 
# popleft() removes left most item - the first. pop() removes right most item - the last
# appendleft() appends to left most part of queue - the beginning. append() adds to right most part of queue - the end
# NOTE: deque is threadsafe! Key for asynchronous programming
friends = deque(('Rolf', 'Jeff', "Kevin"))
friends.appendleft('George')
friends.append('Corey')
friends.pop()
print(friends)