'''
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
'''

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += (i ** 2)
    return sum


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)