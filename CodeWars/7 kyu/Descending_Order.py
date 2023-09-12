'''
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
'''

def descending_order(num):
    num = [int(i) for i in str(num)]
    result = []
    while num:
        result.append(max(num))
        num.remove(max(num))
    return int(''.join(map(str, result)))


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))