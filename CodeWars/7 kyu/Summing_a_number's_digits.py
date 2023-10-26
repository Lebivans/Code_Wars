'''
https://www.codewars.com/kata/52f3149496de55aded000410/train/python
'''

def sum_digits(number):
    result = 0
    if number < 0:
        number *= (-1)
    for i in str(number):
        result += int(i)
    return result


def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))