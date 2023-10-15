'''
https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
'''

def is_valid_walk(walk):
    coordinate = [0, 0]
    if len(walk) != 10:
        return False
    else:
        for i in walk:
            if i == 'n':
                coordinate[1] += 1
            elif i == 's':
                coordinate[1] -= 1
            elif i == 'w':
                coordinate[0] -= 1
            elif i == 'e':
                coordinate[0] += 1
    return coordinate == [0, 0]


def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')