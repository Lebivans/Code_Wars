'''
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
'''

def century(year):
    for i in range(1000):
        if year / 100 == i:
            return i
        if year // 100 == i:
            return i + 1


def century(year):
    return (year + 99) // 100