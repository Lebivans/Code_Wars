'''
https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
'''

def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return 'Underweight'
    elif 18.5 < bmi <= 25:
        return 'Normal'
    elif 25 < bmi <= 30:
        return 'Overweight'
    else:
        return 'Obese'