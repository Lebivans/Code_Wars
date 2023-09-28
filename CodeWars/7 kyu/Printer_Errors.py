'''
https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
'''

def printer_error(s):
    counter = 0
    for i in s:
        if i > 'm':
            counter += 1
    return str(counter) + '/' + str(len(s))


from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))