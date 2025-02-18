import heapq
from typing import List, Dict, Tuple

# Constants for grid representation
START = 'S'
END = 'E'
OBSTACLE = 'X'
FREE = '.'

# Package structure
type Package = Dict[str, any]
type Grid = List[List[str]]

class DeliverySystem:
    def __init__(self, packages: List[Package], grid: Grid):
        self.packages = packages
        self.grid = grid
        self.start = self.find_point(START)
        self.end = self.find_point(END)

    def find_point(self, point: str) -> Tuple[int, int]:
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell == point:
                    return (row_idx, col_idx)
        raise ValueError(f"Point {point} not found in grid")

    def prioritize_packages(self):
        # Priority sorting: urgency (1 = highest priority) > weight
        self.packages.sort(key=lambda p: (p['urgency'], -p['weight']))

    def find_path(self) -> List[Tuple[int, int]]:
        """Implements A* algorithm to find the shortest path."""
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # Cardinal directions
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal directions
        ]
        open_set = []  # Priority queue for A*
        heapq.heappush(open_set, (0, self.start))  # (cost, position)
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.end)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)

                if not self.is_valid_cell(neighbor):
                    continue

                tentative_g_score = g_score[current] + (1.414 if abs(dx) + abs(dy) == 2 else 1)  # Diagonal = 1.414

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.end)
                    if neighbor not in [x[1] for x in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []  # No path found

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        """Euclidean distance heuristic."""
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

    def is_valid_cell(self, cell: Tuple[int, int]) -> bool:
        row, col = cell
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] != OBSTACLE

    def reconstruct_path(self, came_from: Dict[Tuple[int, int], Tuple[int, int]], current: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        return path[::-1]

    def display_grid(self, path: List[Tuple[int, int]]):
        """Displays the grid with the path marked."""
        if not path:
            print("No path to display.")
            return
        grid_copy = [row[:] for row in self.grid]
        for r, c in path:
            if grid_copy[r][c] not in (START, END):
                grid_copy[r][c] = '*'
        for row in grid_copy:
            print(' '.join(row))

# Example Usage
packages = [
    {"id": "PKG001", "urgency": 3, "weight": 10, "description": "An Elephant"},
    {"id": "PKG002", "urgency": 5, "weight": 2, "description": "A Tiny Elephant"},
    {"id": "PKG003", "urgency": 1, "weight": 7, "description": "Child Labourers"},
    {"id": "PKG004", "urgency": 2, "weight": 4, "description": "Drinking Water"},
    {"id": "PKG005", "urgency": 2, "weight": 6, "description": "Chinese Propaganda Books"}
]

grid = [
    ['.', '.', 'X', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.'],
    ['.', 'X', 'X', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['X', 'X', 'X', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', 'X', '.', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', '.', 'S', 'X', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    ['X', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', '.', 'X', '.', '.'],
    ['X', '.', '.', 'X', '.', 'X', '.', 'X', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.', '.', '.'],
    ['X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', 'E', '.', 'X', '.', '.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
    ['X', '.', '.', 'X', '.', 'X', '.', '.', 'X', '.', 'X', '.', '.', 'X', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', 'X', '.', 'X', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', 'X', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.']
]

delivery_system = DeliverySystem(packages, grid)
delivery_system.prioritize_packages()

print("Prioritized Packages:")
for pkg in delivery_system.packages:
    print(pkg)

print("\nFinding Path...")
path = delivery_system.find_path()
delivery_system.display_grid(path)
