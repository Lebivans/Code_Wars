'''
https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
'''

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"


def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"


def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'