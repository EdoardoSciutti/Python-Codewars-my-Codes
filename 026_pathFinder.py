def path_finder(maze):
    maze = maze.split("\n")
    N = len(maze)
    stack = [(0, 0)]
    visited = set((0, 0))

    while stack:
        x, y = stack.pop()
        if (x, y) == (N-1, N-1):
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == '.' and (nx, ny) not in visited:
                stack.append((nx, ny))
                visited.add((nx, ny))

    return False