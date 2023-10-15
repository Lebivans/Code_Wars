'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
'''

from math import prod
def persistence(n):
    step = 0
    while n > 9:
        n = prod([int(i) for i in str(n)])
        step += 1
    return step