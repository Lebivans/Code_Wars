'''
https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python
'''

def stringy(size):
    step = 0
    result = []
    while step != size:
        step += 1
        if step % 2 == 0:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def stringy(size):
    return ('10' * size)[:size]