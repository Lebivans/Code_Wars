'''
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
'''

def row_sum_odd_numbers(n):
    step = 1
    amount = 1
    while step != n:
        amount += 2 * step
        step += 1
    result = amount
    move = n - 1
    increment = 2
    while move != 0:
        result += increment + amount
        increment += 2
        move -=1
    return result


def row_sum_odd_numbers(n):
    return n ** 3