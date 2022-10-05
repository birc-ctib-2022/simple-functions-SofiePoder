"""Exercises with simple functions"""


from calendar import c


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    return a*b*c
...

a = 1
def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    42
    """
    c = a
    return prod(a,b,c)

...


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    if len(x) > len(y):
        return x
    else:
        return y
...

from math import sqrt

def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    7.211102550927978
    """
    x1, y1 = p1
    x2, y2 = p2
    x = (x1+x2)**2
    y = (y1+y2)**2
    sq = sqrt(x+y)
    return sq

...

