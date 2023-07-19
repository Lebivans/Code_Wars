'''
https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
'''

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)