# Task 3: 8 Puzzle using A* Search
class PuzzleState:

    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.f = 0

    # Find empty space
    def find_zero(self):

        for i in range(3):
            for j in range(3):

                if self.board[i][j] == 0:
                    return i, j

    # Generate possible next states
    def generate_children(self):

        children = []

        x, y = self.find_zero()

        moves = [
            (x-1, y, "Up"),
            (x+1, y, "Down"),
            (x, y-1, "Left"),
            (x, y+1, "Right")
        ]

        for nx, ny, move in moves:

            if 0 <= nx < 3 and 0 <= ny < 3:

                # Copy board manually
                new_board = []

                for row in self.board:
                    new_board.append(row[:])

                # Swap empty space with adjacent tile
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                child = PuzzleState(
                    new_board,
                    self,
                    move,
                    self.depth + 1
                )

                children.append(child)

        return children


# Heuristic function
def heuristic(board, goal):

    misplaced = 0

    for i in range(3):
        for j in range(3):

            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                misplaced += 1

    return misplaced


# A* Search
def a_star_search(start, goal):

    open_list = []
    closed_list = []

    start_state = PuzzleState(start)

    start_state.f = heuristic(start, goal)

    open_list.append(start_state)

    while len(open_list) > 0:

        # Find minimum f value
        min_index = 0

        for i in range(1, len(open_list)):

            if open_list[i].f < open_list[min_index].f:
                min_index = i

        # Remove minimum f value state
        current = open_list[min_index]

        open_list.pop(min_index)

        # Check goal
        if current.board == goal:

            path = []

            while current.parent is not None:

                path.append(current.move)

                current = current.parent

            path.reverse()

            return path

        # Add current board to closed list
        closed_list.append(current.board)

        # Generate children
        children = current.generate_children()

        for child in children:

            # Check if already explored
            if child.board not in closed_list:

                child.f = child.depth + heuristic(child.board, goal)

                open_list.append(child)

    return None


# Initial State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Perform A* Search
solution = a_star_search(start, goal)

if solution is not None:

    print("Solution Found!")
    print("Total Moves:", len(solution))
    print("Moves:", solution)

else:

    print("No Solution Found!")









    