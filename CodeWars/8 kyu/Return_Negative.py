'''
https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
'''

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