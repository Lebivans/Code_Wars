'''
https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/python
'''

def goals(laLiga, copaDelRey, championsLeague):
    return (laLiga + copaDelRey + championsLeague)


def goals(*a):
    return sum(a)