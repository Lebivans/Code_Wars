'''
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
'''

def find_short(s):
    quantity = []
    s = s.split()
    for i in s:
        quantity.append(len(i))
    return min(quantity)


def find_short(s):
    return min(len(x) for x in s.split())