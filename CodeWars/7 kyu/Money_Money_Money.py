'''
https://www.codewars.com/kata/563f037412e5ada593000114/train/python
'''

def calculate_years(principal, interest, tax, desired):
    n = 0
    while principal < desired:
        principal += (principal * interest) - (principal * interest * tax)
        n += 1
    return n