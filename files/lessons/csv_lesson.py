file = open('csv_data.txt', 'r')
# Get line as string, without the \n char
csv_lines = [line.strip() for line in file.readlines()]
file.close()

# Read all lines except the header line - line 0
csv_lines = csv_lines[1:]

def get_line_data(data):
    student_list = []
    for line in data:
        line_data = line.split(',')
        name = line_data[0].title()
        age = line_data[1]
        university = line_data[2].title()
        degree = line_data[3].capitalize()
        student_list.append(f'{name} studied {degree} at {university}. They are {age} years old!')

    return student_list

students = get_line_data(csv_lines)
for student in students:
    print(student)