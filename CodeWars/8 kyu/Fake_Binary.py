'''
https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
'''

def fake_bin(string):
    return ''.join('0' if int(i) < 5 else '1' for i in string)

