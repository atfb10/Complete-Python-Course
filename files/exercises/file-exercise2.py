"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# Load questions
question_file = open('questions.txt', 'r')
question_data = [question.strip() for question in question_file.readlines()]
question_file.close()

user_score = 0
max_score = len(question_data)

# Print everything except what comes after =
# If user enters what comes after equals add 1
substring = '='
for question in question_data:
    q_and_a = question.split(substring)
    q = q_and_a[0] + substring
    correct_answer = q_and_a[1]
    user_answer = input(q)

    if user_answer == correct_answer: 
        user_score += 1

results_file = open('results.txt', 'w')
results_file.write(f'Your final score is {user_score}/{max_score}')
results_file.close()