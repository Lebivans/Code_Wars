'''
https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python
'''

def reverse_letter(string):
    result = []
    for i in string:
        if 'a' <= i <= 'z':
            result.append(i)
    return ''.join(result[::-1])


def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]