'''
https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
'''

def remove_url_anchor(url):
    for i in url:
        if i == "#":
            n = url.index(i)
            return url[0:n]
    return url


def remove_url_anchor(url):
    return url.split('#')[0]