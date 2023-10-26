'''
https://www.codewars.com/kata/5547929140907378f9000039/train/python
'''

def shortcut(s):
    result = []
    for i in s:
        if i not in 'aeiou':
            result.append(i)
    return ''.join(result)


def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')