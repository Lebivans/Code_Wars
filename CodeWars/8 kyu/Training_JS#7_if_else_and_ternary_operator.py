'''
https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/python
'''

def sale_hotdogs(n):
    return 100 * n if n < 5 else 95 * n if n >= 5 and n < 10 else n * 90


def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)