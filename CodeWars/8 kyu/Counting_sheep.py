'''
https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
'''

def count_sheeps(sheep):
    quantity = 0
    for x in sheep:
        if x == True:
            quantity += 1
    return quantity


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)