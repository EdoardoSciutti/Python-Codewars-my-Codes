import re

def increment_string(strng):
    match = re.search(r'(\d+)$', strng)
    if match:
        number = match.group(1)
        strng = strng[:-len(number)]
        number = str(int(number) + 1).zfill(len(number))
        return strng + number
    else:
        return strng + '1'