from abc import ABCMeta, abstractmethod
        
class Animal:
    def walk(self) -> None:
        print('walking...')

    # Putting an abstract method in a class makes the class an abstract class. You cannot create an object of Animal
    # It tells you, that whatever class that inherits from Animal, must have the method number_legs()
    @abstractmethod
    def number_legs(self):
        pass
    
class Dog(Animal):
    def __init__(self, name: str):
        self.name = name

    def number_legs(self) -> int:
        return 4

class Monkey(Animal):
    def __init__(self, name: str):
        self.name = name

    def number_legs(self) -> int:
        return 2

animals = [Dog('Scooby'), Monkey('Cheeky')]
for animal in animals:
    print(animal.number_legs())

# Both objects, Dog and Monkey, are instances of Animal
print(isinstance(animals[0], Animal))
print(isinstance(animals[1], Animal))

# They are also instances of their own class
print(isinstance(animals[0], Dog))
print(isinstance(animlas[1], Monkey))