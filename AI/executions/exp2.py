from collections import deque

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    visited = set()           # To track visited nodes
    queue = deque([start])    # Initialize the queue
    path = []                 # To store the traversal path

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)
            path.append(node)

            if node == goal:
                print("Goal found:", path)
                return path

            # Enqueue unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print("Goal not found")
    return None


# Depth-First Search (DFS)
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        print("Goal found:", path)
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()  # Backtrack
    return None


# Example graph and test
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5']
}

start = '1'
goal = '6'

print("Breadth-First Search:")
bfs(graph, start, goal)

print("\nDepth-First Search:")
dfs(graph, start, goal)
