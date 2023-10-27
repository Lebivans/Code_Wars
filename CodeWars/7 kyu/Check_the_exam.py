'''
https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
'''

def check_exam(arr1,arr2):
    score = 0
    n = 0
    while n != 4:
        if arr1[n] == arr2[n]:
            score += 4
        elif arr2[n] == '':
            score += 0
        elif arr1[n] != arr2[n]:
            score -= 1
        n += 1
    return score if score > 0 else 0