'''
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
'''

def alphabet_position(text):
    result = []
    for i in text.lower():
        if 97 <= ord(i) <= 122:
            result.append(ord(i) - 96)
    return ' '.join([str(i) for i in result])


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())