'''
https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
'''

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result


import math
def grow(arr):
    return math.prod(arr)

