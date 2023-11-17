import re

def to_camel_case(text):
    words = re.split('-|_', text)
    return words[0] + ''.join(word.capitalize() for word in words[1:])