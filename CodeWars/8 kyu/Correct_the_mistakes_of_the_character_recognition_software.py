'''
https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python
'''

def correct(s):
    for i in s:
        if i == '5':
            s = s.replace('5', 'S')
        elif i == '0':
            s = s.replace('0', 'O')
        elif i == '1':
            s = s.replace('1', 'I')
    return s   


def correct(string):
    return string.translate(str.maketrans("501", "SOI"))