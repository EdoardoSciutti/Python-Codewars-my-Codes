from collections import deque

def find_shortest_path(grid, start_node, end_node):
    queue = deque([start_node])
    path = {start_node: None}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while queue:
        node = queue.popleft()
        if node == end_node:
            path_list = []
            while node is not None:
                path_list.append(node)
                node = path[node]
            return path_list[::-1]

        for dx, dy in directions:
            x, y = node.position.x + dx, node.position.y + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                neighbor = grid[x][y]
                if neighbor.passable and neighbor not in path:
                    queue.append(neighbor)
                    path[neighbor] = node

    return []