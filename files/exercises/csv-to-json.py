# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# This is what the format should look like...
# [{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, {"club": "Juventus", "country": "Italy", "city": "Turin"}]

import json

# Read in data
file = open('csv-to-json.txt', 'r')
lines = [line.strip() for line in file.readlines()]
file.close()

def csv_to_json_format(data):
    '''
    read in list of csv lines
    extract each element of csv line
    create dictionary object
    return list of dictionaries
    '''
    futbal_teams = []
    for line in data:
        team_data = line.split(',')
        club = team_data[0]
        city = team_data[1]
        country = team_data[2]
        team = {'club': club, 'country': country, 'city': city}
        futbal_teams.append(team)
    return futbal_teams

file_to_write = open('json_file.txt', 'w')
json.dump(csv_to_json_format(lines), file_to_write)
file_to_write.close()