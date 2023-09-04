'''
https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python
'''

def powers_of_two(n):
    result = []
    for i in range(0, n + 1):
        result.append(2 ** i)
    return result


def powers_of_two(n):
    return [2**x for x in range(n+1)]