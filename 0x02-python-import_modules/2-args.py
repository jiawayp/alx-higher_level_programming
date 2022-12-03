#!/usr/bin/python3
import sys
"""Print the number of and the list of arguements
"""
if __name__ == '__main__':
    av = sys.argv
    count_av = len(av) - 1
    if count_av > 1:
        print(count_av, 'arguments: ')
        for i in range(1, count_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif count_av == 1:
        print(count_av, 'argument: ')
        for i in range(1, count_av + 1):
            print('{:d}: {av[i]}'.format(i, av[i]))
    elif count_av == 0:
        print(count_av, 'arguments.')
