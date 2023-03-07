# Open & Read content of data file
my_file = open('data.txt', 'r') # r stands for read
file_content = my_file.read()

# Close the file
my_file.close()

print(file_content)

# Get data to write to file
user = input("what is your name? ")

# Write new data to file
file_writing = open('data.txt', 'w') # w mode overwrites data that was in file previously
file_writing.write(user)
file_writing.write('adam')

# Always remember to close the file!
file_writing.close()