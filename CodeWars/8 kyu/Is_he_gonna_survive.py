'''
https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
'''

def hero(bullets, dragons):
    if bullets == 0:
        return False
    elif dragons == 0:
        return False
    elif bullets / dragons >= 2:
        return True
    else:
        return False


def hero(bullets, dragons):
    return bullets >= dragons * 2