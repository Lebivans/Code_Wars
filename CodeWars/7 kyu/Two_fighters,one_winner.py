'''
https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python
'''

def declare_winner(fighter1, fighter2, first_attacker):
    while fighter2.health > 0 and fighter1.health > 0:
        if first_attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0 or fighter1.health <= 0:
                break
            fighter1.health -= fighter2.damage_per_attack
            if fighter2.health <= 0 or fighter1.health <= 0:
                break
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter2.health <= 0 or fighter1.health <= 0:
                break
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0 or fighter1.health <= 0:
                break
    return fighter2.name if fighter1.health <= 0 else fighter1.name