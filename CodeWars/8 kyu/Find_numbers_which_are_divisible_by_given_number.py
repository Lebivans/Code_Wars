'''
https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
'''

def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result


def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]