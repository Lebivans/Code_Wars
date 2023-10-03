'''
https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
'''

def gimme(input_array):
    array_copy = sorted(input_array.copy())
    i = array_copy[1]
    return input_array.index(i)


def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])