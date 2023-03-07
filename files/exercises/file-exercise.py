# Little Challenge... 
# Ask user for a list of 3 friends
# For each friend we'll tell the user if they are nearby
# For each nearby friend, save name to copy-files-dump.txt
user_data = []
user_data.append(input('Friend 1: '))
user_data.append(input('Friend 2: '))
user_data.append(input('Friend 3: '))

# Open, close files
data_file = open('data.txt', 'r')
data = [line.strip() for line in data_file.readlines()] # line.strip() removes the \n character at the end of each item in the list
data_file.close()

def users_in_data(users, clean_data) -> set:
    '''
    turn lists into sets and check intersection
    originally did it with lists and it worked perfectly!
    This is just less code
    '''
    user_set = set(users)
    data_set = set(clean_data)
    return user_set.intersection(data_set)

def write_name_by_line(file, write_set) -> None:
    index = 0
    for name in write_set:
        index += 1
        if index < len(write_set):
            file.write(f'{name}\n')
        else: file.write(f'{name}')
    return

duplicate_set = users_in_data(user_data, data)
write_file = open('text-file-dump.txt', 'w')
write_name_by_line(write_file, duplicate_set)
write_file.close()