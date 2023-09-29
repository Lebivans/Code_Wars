'''
https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
'''

def divisors(integer):
    result = []
    step = 2
    while step != integer:
        if integer / step == int(integer / step):
            result.append(step)
        step += 1
    return result if len(result) > 0 else f'{integer} is prime'


def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l