def count_patterns_from(firstPoint, length):
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    jumps = [[0]*10 for _ in range(10)]
    jumps[1][3] = jumps[3][1] = 2
    jumps[4][6] = jumps[6][4] = 5
    jumps[7][9] = jumps[9][7] = 8
    jumps[1][7] = jumps[7][1] = 4
    jumps[2][8] = jumps[8][2] = 5
    jumps[3][9] = jumps[9][3] = 6
    jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5
    count = 0
    visited = [False]*10

    def DFS(current, remaining):
        nonlocal count
        if remaining == 0:
            count += 1
            return
        visited[current] = True
        for next in range(1, 10):
            if not visited[next] and (jumps[current][next] == 0 or visited[jumps[current][next]]):
                DFS(next, remaining - 1)
        visited[current] = False

    DFS(grid[(ord(firstPoint) - ord('A')) // 3][(ord(firstPoint) - ord('A')) % 3], length - 1)
    return count