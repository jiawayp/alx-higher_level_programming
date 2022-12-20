#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_n = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and print_n != x:
                    print("{:d}".format(my_list[x]), end ='')
                    print_n += 1
        except TypeError:
            continue
        print()
    return print_n
