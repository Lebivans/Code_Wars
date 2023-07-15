'''
https://www.codewars.com/kata/50654ddff44f800200000004/train/python
'''

def multiply(a, b):
  return a * b

def make_negative( number ):
    if number > 0:
        return number * (-1)
    elif number <0:
        return number
    elif number == 0:
        return 0

# Более простые варианты

def make_negative( number ):
    return -abs(number)


def make_negative( number ):
    return -number if number>0 else number


def make_negative( number ):
    return (-1) * abs(number)