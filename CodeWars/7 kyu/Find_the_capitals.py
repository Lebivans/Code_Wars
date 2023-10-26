'''
https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
'''

def capitals(word):
    result = []
    for i in range(0, len(word)):
        if 'A' <= word[i] <= 'Z':
            result.append(i)
    return result