def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]

    return (a[0] + b[0], a[1] + b[1])
