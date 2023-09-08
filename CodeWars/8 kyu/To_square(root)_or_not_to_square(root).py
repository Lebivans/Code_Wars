'''
https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python
'''

def square_or_square_root(arr):
    result = []
    for i in arr:
        if i ** 0.5 == int(i ** 0.5):
            result.append(i ** 0.5)
        else:
            result.append(i ** 2)
    return result


def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result