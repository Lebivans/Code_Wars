'''
https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
'''

def remove_smallest(numbers):
    listik = numbers.copy()
    if len(listik) == 0:
        return []
    else:
        listik.remove(min(listik))
    return listik