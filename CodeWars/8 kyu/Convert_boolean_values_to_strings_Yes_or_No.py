'''
https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
'''

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    elif boolean == False:
        return 'No'


def bool_to_word(bool):
    return "Yes" if bool else "No"