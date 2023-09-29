'''
https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
'''

def number(lines):
    step = 1
    result = []
    while step != len(lines) + 1:
        for i in lines:
            result.append(str(step) + ': ' + i)
            step += 1
    return result


def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]