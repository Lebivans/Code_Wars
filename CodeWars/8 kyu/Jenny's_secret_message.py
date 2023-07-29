'''
https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python
'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)