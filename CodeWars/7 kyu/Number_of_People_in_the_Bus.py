'''
https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
'''

def number(bus_stops):
    result = 0
    for i in bus_stops:
        result = result + i[0] - i[1]
    return result


def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])