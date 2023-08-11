'''
https://www.codewars.com/kata/515e188a311df01cba000003/train/python
'''

def get_planet_name(id):
    switch = { 2: "Venus",
              1: "Mercury",
              3: "Earth",
              4: "Mars",
              5: "Jupiter",
              6: "Saturn",
              7: "Uranus",
              8: "Neptune"}
    return switch[id]


def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)