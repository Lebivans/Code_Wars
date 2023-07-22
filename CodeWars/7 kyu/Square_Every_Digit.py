'''
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
'''

def square_digits(num):
    digits = [int(i) for i in str(num)]
    digits = [i ** 2 for i in digits]
    digits = map(str, digits)   
    digits = ''.join(digits)          
    digits = int(digits)              
    return digits


def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))