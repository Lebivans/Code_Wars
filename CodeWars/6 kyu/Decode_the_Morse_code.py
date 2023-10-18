'''
https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python
'''

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    message = "".join([MORSE_CODE[i] if i in MORSE_CODE else " " for i in morse_code.split(" ")])
    return message.replace("  ", " ").strip()