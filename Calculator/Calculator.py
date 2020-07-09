from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
#from Calculator.square import square
#from Calculator.squareroot import squareroot

import math


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    
    def divide(self, a, b): 
        self.result = division(a, b)
        return self.result  

    def square(self, a): 
        self.result = square(a)
        return self.result  
    
    def sqrt(self, a):
        self.result = math.sqrt(a)
        # self.result = power(base, 2)
        return self.result
    

