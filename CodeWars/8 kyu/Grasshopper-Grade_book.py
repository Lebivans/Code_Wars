'''
https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
'''

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 0 <= score < 60:
        return 'F'
    elif 60 <= score < 70:
        return 'D'
    elif 70 <= score < 80:
        return 'C'
    elif 80 <= score < 90:
        return 'B'
    else:
        return 'A'


def get_grade(*scores):
    grades = {
        10: 'A',
        9: 'A',
        8: 'B',
        7: 'C',
        6: 'D',
    }
    mean = sum(scores) / len(scores)
    return grades.get(mean // 10, 'F')