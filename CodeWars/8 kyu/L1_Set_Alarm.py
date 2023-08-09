'''
https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
'''

def set_alarm(employed, vacation):
    return True if employed == True and vacation == False else False


def set_alarm(employed, vacation):
    return employed and not vacation