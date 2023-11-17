import re

def spin_words(sentence):
    words = re.split(' ', sentence)
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
        
    return ' '.join(words)