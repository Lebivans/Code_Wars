'''
https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python
'''

def well(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') < 3:
        return 'Publish!'
    else:
        return 'I smell a series!'