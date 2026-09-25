"""
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class square(shape):
    def __init__(self, side):
        self.__side =side
        
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class square(shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side* self.__side

    def perimeter(self):
        return 4 * self.__side

#myshape = shape()

mysquare = square(5)

print(mysquare.area())
print(mysquare.perimeter())
"""

from datetime import datetime
from datetime import date


