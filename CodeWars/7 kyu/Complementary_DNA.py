'''
https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
'''

import re
def DNA_strand(dna):
    result = {'C':'G', 'G':'C', 'A':'T', 'T':'A'}
    table = str.maketrans(result)
    return dna.translate(table)


def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])