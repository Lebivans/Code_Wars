'''
https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python
'''

def max_multiple(divisor, bound):
    numbers = []
    for i in range(divisor, bound + 1):
        if i % divisor == 0:
            numbers.append(i)
    return max(numbers)