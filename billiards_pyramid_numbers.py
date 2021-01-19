# Author: Martin Luther Bironga
# Date: 29/1/2021

# problem statement
"""
Remember the pyramid of balls in billiards? To build a classic pyramid (5 levels) you need 15 balls. With 3 balls you can build a 2-level pyramid, etc.

For more examples,

pyramid(1) == 1

pyramid(3) == 2

pyramid(6) == 3

pyramid(10) == 4

pyramid(15) == 5
Write a function that takes number of balls (≥ 1) and calculates how many levels you can build a pyramid.
"""

# solution
from functools import reduce

def pyramid(balls):
        list_balls=list(range(1,balls+1))
        cumsum_list=reduce(lambda c, x: c + [c[-1] + x], list_balls, [0])[1:]
        filter_list=[i for i in cumsum_list if i<=balls]
        return len(filter_list)



# variations
pyramid = lambda b: int(0.5*(-1+(1+8*b)**0.5))

import math
def pyramid(balls):
    return abs(int(0.5*(-1+math.sqrt(1+balls*8))))

pyramid = lambda b: next(i - 1 for i in range(b + 2) if sum(range(i + 1)) > b)
