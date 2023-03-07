# 'With' automatically opens and closes file for you, so you do not forget to close it
import json

# Example A
with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)

# Write to json file
cars = [
    {'make': 'ford', 'model': 'focus'},
    {'make': 'tesla', 'model': 'model s'},
    {'make': 'ford', 'model': 'tacoma'},
    {'make': 'gmc', 'model': 'sierra'}
]

# Example B
with open('json_dump_lesson.txt', 'w') as write_file:
    json.dump(cars, write_file)