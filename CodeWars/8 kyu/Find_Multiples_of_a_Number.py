'''
https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python
'''

def find_multiples(integer, limit):
    result = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            result.append(i)
    return result