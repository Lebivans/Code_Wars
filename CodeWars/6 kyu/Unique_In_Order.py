'''
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
'''

def unique_in_order(sequence):
    result = []
    if len(sequence) > 0:
        result.insert(1, sequence[0])
    elif len(sequence) == 0 or sequence == "":
        return []
    for i in range(1, len(sequence)):
            try:
                if sequence[i] != sequence[i-1] and sequence != sequence[i+1]:
                    result.append(sequence[i])
            except:
                if sequence[i] != sequence[i-1]:
                    result.append(sequence[i])
    return result


def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result