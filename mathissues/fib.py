

def fib(subscript):
    x = 1
    y = 1
    if subscript < 2:
        return 1
    i = 0
    while i < subscript:
        y = y + x
        x = y - x
        i = i + 1
    return y
