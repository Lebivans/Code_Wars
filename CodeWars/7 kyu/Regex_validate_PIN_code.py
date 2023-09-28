'''
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
'''

def validate_pin(pin):
    try:
        pin = [int(i) for i in pin]
    except:
        return False
    return len(pin) == 4 or len(pin) == 6


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()