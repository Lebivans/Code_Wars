'''
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
'''


def duplicate_count(text):
    text = [i.lower() for i in text]
    text_2 = []
    for i in text:
        if text.count(i) > 1:
            if i.isdigit():
                if i not in text_2:
                    text_2.append(i)
                else:
                    continue
            else:
                if i.lower() not in text_2:
                    text_2.append(i.lower())
                else:
                    continue
    return len(text_2)


def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])