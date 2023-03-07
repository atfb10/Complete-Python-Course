# Lambda functions are used to get inputs, do processing & return outputs

divide = lambda x, y: x / y

print(divide(10, 2))

grades = [90, 98, 100, 75]
average = lambda grades: sum(grades) / len(grades)

print(average(grades))

say_hello: lambda name: print(f'Hello {name}')
say_hello('bart')

square_number = lambda value: value ** 2