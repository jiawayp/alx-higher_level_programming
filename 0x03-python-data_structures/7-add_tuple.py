def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from tuple_a and tuple_b
    a = tuple_a[:2]
    b = tuple_b[:2]

    # Pad the tuples with 0 if they have less than 2 elements
    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))

    # Perform the element-wise addition
    result = (a[0] + b[0], a[1] + b[1])

    return result
