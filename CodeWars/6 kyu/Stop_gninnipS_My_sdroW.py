'''
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
'''

def spin_words(sentence):
    sentence = sentence.split()
    result = []
    for i in sentence:
        if len(i) < 5:
            result.append(i)
        else:
            result.append(i[::-1])
    return ' '.join(result)


def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])