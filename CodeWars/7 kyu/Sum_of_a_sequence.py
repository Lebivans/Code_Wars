'''
https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
'''

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        return sum(range(begin_number, end_number + 1, step))


def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))