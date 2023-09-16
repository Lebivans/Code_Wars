'''
https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
'''

def xo(s):
    x = 0
    o = 0
    for i in s.lower():
        if i == 'x':
            x += 1
        elif i == 'o':
            o += 1
    return x == o


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')