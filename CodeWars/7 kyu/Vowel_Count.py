'''
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
'''


def get_count(sentence):
    quantity = 0
    for x in sentence:
        if x == 'a':
            quantity += 1
        elif x == 'e':
            quantity += 1
        elif x == 'i':
            quantity += 1
        elif x == 'o':
            quantity += 1
        elif x == 'u':
            quantity += 1
    return quantity


def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")