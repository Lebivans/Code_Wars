'''
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
'''

def count_positives_sum_negatives(arr):
    quantity = 0
    sum = 0
    for x in arr:
        if x > 0:
            quantity += 1
        else:
            sum += x
    if len(arr) < 0 or arr == []:
        return []
    else:
        return [quantity, sum]


def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []