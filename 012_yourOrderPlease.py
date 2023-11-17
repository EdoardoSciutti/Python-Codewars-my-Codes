def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    sorted_words = [None] * len(words)
    
    for word in words:
        for char in word:
            if char.isdigit():
                sorted_words[int(char) - 1] = word
                
    return ' '.join(sorted_words)