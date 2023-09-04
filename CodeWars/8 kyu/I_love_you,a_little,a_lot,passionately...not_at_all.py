'''
https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python
'''

def how_much_i_love_you(nb_petals):
    test = 1
    quantity = 1
    phrases = {1: "I love you",
              2: "a little",
              3: "a lot",
              4: "passionately",
              5: "madly",
              6: "not at all"}
    
    while test != nb_petals:
        if quantity == 6:
            quantity = 1
        else:
            quantity += 1
        test += 1
    return phrases[quantity]


phrases = [
    'I love you',
    'a little',
    'a lot',
    'passionately',
    'madly',
    'not at all',
]

def how_much_i_love_you(n):
    return phrases[(n - 1) % len(phrases)]