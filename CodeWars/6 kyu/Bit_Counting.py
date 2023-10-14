'''
https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
'''

def count_bits(n):
    n = '{0:08b}'.format(n)
    n = [int(i) for i in n]
    quantity = 0
    for i in n:
        if i == 1:
            quantity += 1
    return quantity


def countBits(n):
    return bin(n).count("1")