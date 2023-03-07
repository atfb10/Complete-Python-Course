import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)
file.close()

print(file_contents['friends'])

# Write to json file
cars = [
    {'make': 'ford', 'model': 'focus'},
    {'make': 'tesla', 'model': 'model s'},
    {'make': 'ford', 'model': 'tacoma'},
    {'make': 'gmc', 'model': 'sierra'}
]

# How to loop over a list of dictionaries
# Loop through each item in the list
# List through each item of the dictionary object
count = 0
for car in cars:
    count += 1
    make = ''
    model = ''
    for key, value in car.items():
        print(f'{key}: {value}')
    print('---------------')

# Save a file as JSON
write_file = open('json_dump_lesson.txt', 'w')
json.dump(cars, write_file)
write_file.close()