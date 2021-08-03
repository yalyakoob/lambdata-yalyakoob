import math
import sys


def exampl1():
    # This is a comment to be used
    some_tuple = (1, 2, 3, 'a')
    some_variable = {"long": 'LONG CODE LINES should be <=79',
                     "other": [math.pi, 100, 200, 300, 9999292929292],
                     "inner": ["THIS whole logical line should be wrapped"],
                     "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]}
    return (some_tuple, some_variable)


def example_2(): return {"has_key() is deprecated": True}


class Example3(object):
    def __init__(self, bar):
        if bar:
            bar += 1
            bar = bar * bar
        return bar
