'''
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
'''

def open_or_senior(data):   
    result =[]
    for i in data: 
        if i[0] >= 55 and i[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result


def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]