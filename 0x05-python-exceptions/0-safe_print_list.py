#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n_list = 0

    try:
        for i in my_list:
            if n_list < x:
                print(f"{my_list[n_list]}", end='')
                n_list = n_list + 1
        print()
    except TypeError:
        pass
    finally:
        return n_list
