'''
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
'''

def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    return str(max(numbers)) + ' ' + str(min(numbers))


def high_and_low(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"