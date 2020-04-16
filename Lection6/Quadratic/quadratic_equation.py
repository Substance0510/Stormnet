#!/usr/bin/python3
r"""
This module returns 2 roots in tupple of a square equation if they exist, and returns False if there are no roots.
>>> quadratic_equation1(3, -14, -5)
(5.0, -0.3333333333333333)
>>> quadratic_equation1(4, -7)
(1.75, 0.0)
>>> quadratic_equation1(1, 2, 17)
False
"""


def quadratic_equation1(a=1, b=0, c=0):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return False
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
	
input()