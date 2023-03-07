import re

'''
. = "anything" - letters, numbers, symbols... but not newlines
+ "one or more of"
* "zero or more of"
? "zero or one of"
'''

email = 'aforestier10@gmail.com'
expression = '[a-z\.]+'

# This will get a list of all times that expression occurs
match = re.findall(expression, email)
print(match)
name = match[0]
domain = match[1]
print(f'name = {name}. domain = {domain}')

price = 'Price: $18,109.50'
expression = 'Price: \$([0-9,]\.[0-9])'

matches = re.search(expression, price)
print(matches.group(0)) # Whole match
print(matches.group(1)) # What is inside parentheses