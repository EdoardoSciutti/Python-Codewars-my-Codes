def alphabet_position(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += str(ord(char.lower()) - 96) + ' '
    return result.rstrip()