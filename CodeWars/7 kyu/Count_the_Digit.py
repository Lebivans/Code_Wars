'''
https://www.codewars.com/kata/566fc12495810954b1000030/train/python
'''

def nb_dig(n, d):
    result = 0
    for i in range(0, n+1):
        result += str(i ** 2).count(str(d))
    return result


def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))