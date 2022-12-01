#!/usr/bin/python3
import sys

def av(): 
    av = sys.argv 
    l_av = len(av) - 1
    if l_av > 1: 
        print(l_av, 'arguments: ') 
        for i in range(1, l_av + 1):
            print(f'{i:d}: {av[i]}')
    elif l_av == 1: 
        print(l_av, 'argument: ')
        for i in range(1, l_av + 1):
            print(f'{i:d}: {av[i]}')
    elif l_av == 0:
        print(l_av, 'arguments.')
av()
