import heapq

# Define a Node class for A* nodes
class Node:
    def __init__(self, state, g, h, parent=None):
        self.state = state      # Current state (e.g., coordinates)
        self.g = g              # Cost from start to current node
        self.h = h              # Heuristic cost to goal
        self.f = g + h          # Total estimated cost
        self.parent = parent    # Pointer to parent node for path reconstruction

    def __lt__(self, other):
        return self.f < other.f  # Priority queue uses this for comparison


# A* Search Algorithm
def a_star(start, goal, heuristic, get_neighbors):
    open_list = []
    closed_list = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_node.state)

        for neighbor in get_neighbors(current_node.state):
            if neighbor in closed_list:
                continue

            g = current_node.g + 1
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g, h, current_node)

            # Only add neighbor if it's not in open list with lower f cost
            if not any(open_node.state == neighbor and open_node.f <= neighbor_node.f
                       for open_node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None


# Manhattan Distance Heuristic
def manhattan_heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


# Neighbor generator (4-directional movement in a 5x5 grid)
def get_neighbors(state):
    x, y = state
    neighbors = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        new_state = (x + dx, y + dy)
        if 0 <= new_state[0] < 5 and 0 <= new_state[1] < 5:  # Grid bounds
            neighbors.append(new_state)
    return neighbors


# Example run
start = (0, 0)
goal = (4, 4)

path = a_star(start, goal, manhattan_heuristic, get_neighbors)

if path:
    print("Path found:", path)
else:
    print("No path found")
