'''
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
'''

def disemvowel(string):
    string = string.replace('a', '')
    string = string.replace('A', '')
    string = string.replace('e', '')
    string = string.replace('i', '')
    string = string.replace('o', '')
    string = string.replace('u', '')
    string = string.replace('E', '')
    string = string.replace('I', '')
    string = string.replace('O', '')
    string = string.replace('U', '')
    return string



def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")