#!/usr/bin/python3
import sys
"""Print the number of and the list of arguements
"""
if __name__ == '__main__':
    av = sys.argv
    c_av = len(av) - 1
    if c_av > 1:
        print(c_av, 'arguments:')
        for i in range(1, c_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif c_av == 1:
        print(c_av, 'argument:')
        for i in range(1, c_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif c_av == 0:
        print(c_av, 'arguments.')
