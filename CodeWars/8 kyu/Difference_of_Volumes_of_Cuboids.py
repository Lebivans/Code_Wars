'''
https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
'''

def find_difference(a, b):
    volum_a = volum_b = 1
    for i in a:
        volum_a *= i
    for i in b:
        volum_b *= i
    return abs(volum_a - volum_b)


def find_difference(a, b):
	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])


# from numpy import prod
# def find_difference(a, b):
#    return abs(prod(a) - prod(b))