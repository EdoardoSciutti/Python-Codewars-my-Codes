def get_count(sentence):
    return sum(1 for char in sentence if char.lower() in 'aeiou')