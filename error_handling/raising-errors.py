class Car:
    def __init__(self, name, model):
        self.name = name 
        self.model = model

    def __repr__(self):
        return f'<{self.name}: {self.model}>'
    

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        # is instance is a built in Python function that takes a variable and class as parameter. It returns a boolean of if the variable is an object of the class
        if not isinstance(car, Car):
            raise TypeError("Must add object of Car class")
        self.cars.append(car)    

car = Car('fiesta', 'ford')
ford = Garage()

# This will raise a type error, because I am passing a string argument instead of a class object argument
ford.add_car('focus')