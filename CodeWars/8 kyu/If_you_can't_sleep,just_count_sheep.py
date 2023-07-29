'''
https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
'''

def count_sheep(n):
    string = ""
    for i in range(1, n + 1):
        string += str(i) + ' sheep...'
    return string


def count_sheep(n):
    sheep=[]
    for i in range(1, n+1):
        sheep.append(str(i) + " sheep...")
    return "".join(sheep)


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))