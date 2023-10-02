'''
https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
'''

def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return len(result)