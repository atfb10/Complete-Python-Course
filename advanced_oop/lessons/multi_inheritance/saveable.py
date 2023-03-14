from db import Database
from abc import ABCMeta, abstractmethod

class Saveable(metaclass=ABCMeta):
    '''
    interface - superclass that defines the functionality that must be in a subclass
    '''
    def save(self):
        Database.insert(self.to_dict())
    
    @abstractmethod
    def to_dict(self):
        '''
        abstract method that must be implemented in any subclass of Saveable
        '''
        pass

    