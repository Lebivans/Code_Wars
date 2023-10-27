'''
https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
'''

def capitalize(s):
    result = []
    for i in range(0, len(s)):
        if i == 0 or i % 2 == 0:
            result.append(s[i].upper())
        else:
            result.append(s[i])
    result.append(' ')
    for i in range(0, len(s)):
        if i % 2 != 0:
            result.append(s[i].upper())
        else:
            result.append(s[i])
    result = ''.join(result)
    return result.split(' ')


def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]