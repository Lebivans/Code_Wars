'''
https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
'''

def is_square(n):
    n_modern = n ** 0.5
    if n < 0:
        return False
    
    if n_modern == int(n_modern):
        result = int(n_modern)
        if isinstance(result, int):
            return True
    else:
        return False


import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;


def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0