def two_sum(numbers, target):
    index_map = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in index_map:
            return (index_map[complement], i)
        else:
            index_map[num] = i
    return ()