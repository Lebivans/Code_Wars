'''
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
'''

def create_phone_number(n):
    n = ''.join([str(i) for i in n])
    return f'({n[:3]}) {n[3:6]}-{n[6:]}'


def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)