'''
https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
'''

def series_sum(n):
    fractions = []
    for n in range(1, 3*n - 1, 3):
        fractions.append(1/n)
    return "{:.2f}".format(sum(fractions))


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))