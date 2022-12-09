#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = dict(a_dictionary)
    for key, value in mul.items():
        mul[key] = value * 2
    return mul
