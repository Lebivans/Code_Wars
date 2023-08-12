'''
https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
'''

def str_count(string, letter):
    quantity = 0
    for i in string:
        if i == letter:
            quantity += 1
    return quantity


def strCount(string, letter):
    return string.count(letter)