class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Garage(Car): 
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
        raise TypeError("Method add_car() must take a Car object as its parameter")
    

class CustomTypeError(TypeError):
    # Below """ """ is a docstring. Really really cool. It does 2 things
    # 1 - Tells developers what the point of the class is
    # 2 - Is included in class object
    
    """
    exception raised when a specific error code is needed
    """

    # msg is built in parameter to TypeError(). It is inherited from TypeError()
    # error_code is a parameter I am adding to this custom TypeError class
    def __init__(self, msg, error_code):
        # Creating CustomTypeError() result when CustomTypeError object is created
        super(TypeError, self).__init__(f'code: {error_code}: {msg}') 
        self.error_code = error_code

# Create custom type error object
err = CustomTypeError('Type error has occurred', 500)

# Use docstring
print(err.__doc__)

# Create car & garage objects
ford = Garage()
car = Car('Ford', 'Fiesta')

# Try/except
try:
    ford.add_car('focus')
except:
    print('Your car is not a car object')
