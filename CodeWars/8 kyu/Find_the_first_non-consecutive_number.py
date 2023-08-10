'''
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python
'''

def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i!=j:
            return j