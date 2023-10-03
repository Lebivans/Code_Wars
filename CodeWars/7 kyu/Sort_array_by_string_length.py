'''
https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python
'''

def sort_by_length(arr):
    result = []
    step = 0
    while len(result) != len(arr):
        for i in arr:
            if len(i) == step:
                result.append(i)
        step += 1
    return result


def sort_by_length(arr):
    return sorted(arr, key=len)