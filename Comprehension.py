# 1. Shows how function comprehension works

def myfunc(*args):
    return [arg for arg in args if arg % 2 == 0]


"""
def myfunc(*args):
    even_numbers = []
    for arg in args:
        if arg % 2 == 0:
            even_numbers.append(arg)
    return even_numbers
"""