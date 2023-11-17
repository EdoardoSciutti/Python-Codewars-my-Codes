def first_non_repeating_letter(s):
    for i in s:
        if s.lower().count(i.lower()) == 1:
            return i
    return ""