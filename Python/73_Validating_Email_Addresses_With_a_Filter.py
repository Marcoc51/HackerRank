import re

def fun(s):
    return re.fullmatch(r'\b[A-Za-z0-9_-]+\@[A-Za-z0-9]+\.[A-Z|a-z]{1,3}\b', s)
