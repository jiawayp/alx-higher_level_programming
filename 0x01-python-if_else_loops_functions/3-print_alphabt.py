#!/usr/bin/python3
for small_alp in range(97, 123):
    if chr(small_alp) not in ['q', 'e']:
        print("{}".format(chr(small_alp)), end="")
