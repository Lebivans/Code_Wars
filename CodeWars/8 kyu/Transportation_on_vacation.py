'''
https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
'''

def rental_car_cost(days):
    price = days * 40
    if days >= 7:
        price -= 50
    elif days >= 3:
        price -= 20
    return price