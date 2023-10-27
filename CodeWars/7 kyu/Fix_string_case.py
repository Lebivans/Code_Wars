'''
https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
'''

def solve(s):
    big = 0
    small = 0
    for i in s:
        if i == i.upper():
            big += 1
        else:
            small += 1
    return s.upper() if big > small else s.lower()