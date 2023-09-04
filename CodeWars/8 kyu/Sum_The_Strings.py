'''
https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
'''

def sum_str(a, b):
    if a == "" and b == "":
        return str(0)
    elif a == "":
        return str(int(0) + int(b))
    elif b == "":
        return str(int(a) + int(0))
    else:
        return str(int(a) + int(b))


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))