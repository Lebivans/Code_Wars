'''
https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
'''

def find_next_square(sq):
    if sq ** 0.5 == int(sq ** 0.5):
        return (int(sq ** 0.5) + 1) ** 2
    else:
        return -1


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1