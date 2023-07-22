'''
https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
'''

def digitize(n):
    return list(reversed([int(i) for i in str(n)]))


def digitize(n):
    return [int(x) for x in str(n)[::-1]]


def digitize(n):
    return [int(x) for x in reversed(str(n))]