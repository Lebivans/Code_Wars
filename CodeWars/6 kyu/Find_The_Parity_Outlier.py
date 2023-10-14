'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
'''

def find_outlier(integers):
    if integers[0] % 2 == 0: # 1 чет
        if integers[1] % 2 == 0: # 2 чет
            for i in integers:
                if i % 2 != 0:
                    return i
        else:                   # 1 чет, 1 нечет
            if integers[2] % 2 == 0: # 2 чет
                for i in integers:
                    if i % 2 != 0:
                        return i
            else:               # 2 нечет
                for i in integers:
                    if i % 2 == 0:
                        return i
    else:                       # 1 нечет
        if integers[2] % 2 != 0: # 2 нечет
                for i in integers:
                    if i % 2 == 0:
                        return i
        else:
            for i in integers:
                    if i % 2 != 0:
                        return i