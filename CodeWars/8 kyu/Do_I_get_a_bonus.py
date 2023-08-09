'''
https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python
'''

def bonus_time(salary, bonus):
    if bonus == True:
        salary *= 10
    return '$' + str(salary)


def bonus_time(salary, bonus):
    return f"${salary * 10 if bonus else salary}"