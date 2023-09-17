'''
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
'''

def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        return '#' * (len(cc) - 4) + cc[-4:] 