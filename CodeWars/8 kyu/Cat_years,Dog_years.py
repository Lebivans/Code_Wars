'''
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
'''

def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    years = 0
    while human_years != years:
        if years >= 2:
            cat_years += 4
            dog_years += 5
            years += 1
        elif years == 1:
            cat_years += 9
            dog_years += 9
            years += 1
        elif years == 0:
            cat_years += 15
            dog_years += 15
            years += 1
    return [human_years, cat_years, dog_years]