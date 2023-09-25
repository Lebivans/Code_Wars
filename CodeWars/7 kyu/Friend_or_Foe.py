'''
https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
'''

def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result


def friend(x):
    return [f for f in x if len(f) == 4]