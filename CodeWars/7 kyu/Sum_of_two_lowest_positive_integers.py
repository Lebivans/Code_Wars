'''
https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
'''

def sum_two_smallest_numbers(numbers):
    result = []
    start = 0
    while start != 2:
        result.append(min(numbers))
        numbers.remove(min(numbers))
        start += 1
    return result[0] + result[1]


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])