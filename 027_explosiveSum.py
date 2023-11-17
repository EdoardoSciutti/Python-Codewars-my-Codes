def exp_sum(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ways[j] += ways[j - i]
    return ways[n]