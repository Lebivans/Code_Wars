'''
https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
'''

def dont_give_me_five(start,end):
    fives = []
    for i in range(start, end + 1):
        if '5' in str(i):
            fives.append(i)
    return len(range(start, end + 1)) - len(fives)