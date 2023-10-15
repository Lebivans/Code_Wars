'''
https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
'''

def to_camel_case(text):
    if len(text) == 0:
        return ""
    else:
        text = text.replace('_', ' ').replace('-', ' ').split(' ')
        text_1 = text[0]
        text = [i.title() for i in text[1:]]
        text.insert(0, text_1)
        return ''.join(text)


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])