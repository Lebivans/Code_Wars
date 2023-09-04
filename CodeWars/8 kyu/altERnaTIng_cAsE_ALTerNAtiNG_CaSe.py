'''
https://www.codewars.com/kata/56efc695740d30f963000557/train/python
'''

def to_alternating_case(string):
    result = ''
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result


def to_alternating_case(string):
    return string.swapcase()