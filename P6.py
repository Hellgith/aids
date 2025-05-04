from collections import deque

# Graph representing landmarks and their connections
landmarks_map = {
    'ICEM Main Gate': ['Avirat Open Parking'],
    'Avirat Open Parking': ['ICEM Main Gate', 'Maggie Point', 'Xerox Shop'],
    'Maggie Point': ['Avirat Open Parking', 'Xerox Shop'],
    'Xerox Shop': ['Maggie Point', 'Avirat Open Parking', 'Workshop'],
    'Workshop': ['Xerox Shop', 'Avirat Open Parking']
}

# BFS to find the shortest path
def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])  # Initialize BFS queue with the starting point
    visited = set()           # Set for visited landmarks

    while queue:
        path = queue.popleft()
        landmark = path[-1]

        if landmark == goal:
            return path

        if landmark not in visited:
            visited.add(landmark)
            for neighbor in graph.get(landmark, []):
                if neighbor not in visited:
                    queue.append(path + [neighbor])

    return None  # If no path found

# DFS to find all paths between two landmarks
def dfs_all_paths(graph, start, goal, path=None):
    if path is None: path = [start]

    if start == goal: return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            paths.extend(dfs_all_paths(graph, neighbor, goal, path + [neighbor]))

    return paths

# Example usage
start_landmark = 'ICEM Main Gate'
end_landmark = 'Workshop'

# Find shortest path using BFS
shortest_path = bfs_shortest_path(landmarks_map, start_landmark, end_landmark)
if shortest_path:
    print(f"Shortest path: {shortest_path}")
else:
    print("No path found")

# Find all paths using DFS
all_paths = dfs_all_paths(landmarks_map, start_landmark, end_landmark)
print("All paths:")
for path in all_paths:
    print(path)
