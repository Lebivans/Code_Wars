'''
https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
'''

def factorial(n):
    result = 1
    if n == 0:
        return 1
    elif n > 0 and n <= 12:
        while n != 0:
            result *= n
            n -= 1
    else:
        raise ValueError
    return result