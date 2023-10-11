'''
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
'''

def digital_root(n):
    if n < 10:
        return n
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digital_root(digit_sum)