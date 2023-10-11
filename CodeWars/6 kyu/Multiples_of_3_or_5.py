'''
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
'''

def solution(number):
    result = 0
    step = 1
    while step != number:
        if number <= 0:
            return 0
        elif step % 3 == 0 or step % 5 == 0:
            result += step
        step += 1
    return result