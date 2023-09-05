'''
https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
'''

def two_sort(array):
    array.sort()
    return '***'.join(array[0])


def two_sort(lst):
    return '***'.join(min(lst))


def two_sort(arr):
    return '***'.join(sorted(arr)[0])