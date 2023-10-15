'''
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
'''

def duplicate_encode(word):
    result = []
    for i in word.lower():
        if word.lower().count(i) > 1:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)