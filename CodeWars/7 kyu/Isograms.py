'''
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
'''

def is_isogram(string):
    return ''.join(sorted(set(string.lower()))) == ''.join(sorted(list(string.lower())))


def is_isogram(string):
    return len(string) == len(set(string.lower()))