'''
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
'''

def accum(s):
    result = []
    counter = 0
    while s:
        for i in s:
            result.append(i.upper() + i.lower() * counter)
            result.append('-') 
            s = s[1:]
            counter += 1
    result.pop(-1)
    return ''.join(result)