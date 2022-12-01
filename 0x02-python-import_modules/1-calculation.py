#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def cal():
    """Prints the result of the addition, substract, multiplication and division between two numbers"""
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
cal()
