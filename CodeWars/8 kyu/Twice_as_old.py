'''
https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python
'''

def twice_as_old(dad_years_old, son_years_old):
    quantity_high = 0
    quantity_low = 0
    dad_age_up = dad_years_old
    dad_age_down = dad_years_old
    son_age_up = son_years_old
    son_age_down = son_years_old
    while dad_age_up <= 100:
        if dad_age_up == son_age_up * 2:
            return quantity_high
        else:
            dad_age_up += 1 
            son_age_up += 1
            quantity_high += 1
    while son_age_down >= 0:
        if dad_age_down == son_age_down * 2:
            return quantity_low
        else:
            dad_age_down -= 1
            son_age_down -= 1
            quantity_low += 1


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)