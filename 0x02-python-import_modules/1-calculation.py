#!/usr/bin/python3
from calculator_1 import add, sub, mul, div 
def cal():
    """ Prints the result of the addition, substract, multiplication and division between two numbers """ 
    a = 10 
    b = 5
    print(f'{a:d} + {b:d} = {add(a, b):d}') 
    print(f'{a:d} - {b:d} = {sub(a, b):d}')
    print(f'{a:d} * {b:d} = {mul(a, b):d}') 
    print(f'{a:d} / {b:d} = {div(a, b):d}')
cal()
