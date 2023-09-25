'''
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
'''

def get_sum(a,b):
    numbers = sorted([a, b])
    return sum(range(numbers[0], numbers[1]+1))


def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))