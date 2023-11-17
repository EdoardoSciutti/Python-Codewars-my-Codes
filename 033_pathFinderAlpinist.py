import heapq

def path_finder(mountain):
    mountain = [list(row) for row in mountain.split('\n')]
    n = len(mountain)
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # cost, row, col
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        cost, row, col = heapq.heappop(pq)
        if row == col == n - 1:
            return cost
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                new_cost = cost + abs(int(mountain[new_row][new_col]) - int(mountain[row][col]))
                if new_cost < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_cost
                    heapq.heappush(pq, (new_cost, new_row, new_col))

    return -1