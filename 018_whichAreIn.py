def in_array(array1, array2):
    result = []
    for s1 in array1:
        for s2 in array2:
            if s1 in s2 and s1 not in result:
                result.append(s1)
    result.sort()
    return result