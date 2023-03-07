def greet():
    print(f'Hello {input("Enter Name: ")}')

greet()
print('\n')

cars = [
    {'make': "ford", 'model': 'fiesta','mileage': 23000,'fuel_consumed': 460},
    {'make': "gmc", 'model': 'sierra','mileage': 44000,'fuel_consumed': 500}
]

def find_make_model(vehicle):
    return f'{vehicle["make"]} {vehicle["model"]}'

make_model = find_make_model(cars[0])
print(make_model)

# get list of vehicle make models
car_make_model = []
for car in cars:
    car_make_model.append(find_make_model(car))

print(car_make_model)
