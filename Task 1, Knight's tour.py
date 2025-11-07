#TASK 1, Knight's Tour
# a) Tomt 8x8-brett
def make_empty_board(n: int = 8):
    return [[0 for _ in range(n)] for _ in range(n)]

def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))

# b) Input-håndtering
def get_user_choice():
    while True:
        print("\n=== Knight's Tour ===")
        print("Choose method:")
        print("1 - Las Vegas")
        print("2 - Backtracking")
        print("3 - Cancel")

        choice = input("Write your choice (1/2/3): ").strip()
        if choice == '1':
            print("\nYou have chosen: Las Vegas-methode\n")
            return "Las Vegas"
        elif choice == '2':
            print("\nYou have chosen: Backtracking-methode\n")
            return "Backtracking"
        elif choice == '3':
            print("\nCanceling programme. Have a nice day!\n")
            raise SystemExit(0)
        else:
            print("\nInvalid choice! Try again (write 1, 2 or 3).")

# i) Las Vegas
import random
from typing import Tuple, List

def KnightsTourLasVegas(startingPosition: Tuple[int, int]) -> tuple[bool, list[list[int]]]:
    board = [[0 for _ in range(8)] for _ in range(8)]
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

    x, y = startingPosition
    if not (0 <= x < 8 and 0 <= y < 8):
        return False, board

    board[x][y] = 1
    for step in range(2, 65):
        possible = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == 0:
                possible.append((nx, ny))
        if not possible:
            return False, board
        x, y = random.choice(possible)
        board[x][y] = step
    return True, board

# ii) Backtracking (uten heuristikk)
def KnightsTourBacktracking(startingPosition: Tuple[int, int]) -> Tuple[bool, List[List[int]]]:
    N = 8
    board = [[0 for _ in range(N)] for _ in range(N)]
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

    x, y = startingPosition
    if not (0 <= x < N and 0 <= y < N):
        return False, board
    board[x][y] = 1

    def is_valid(nx: int, ny: int) -> bool:
        return 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0

    def solve(step: int, x: int, y: int) -> bool:
        if step > N * N:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                board[nx][ny] = step
                if solve(step + 1, nx, ny):
                    return True
                board[nx][ny] = 0
        return False

    success = solve(2, x, y)
    return success, board

# c) Tekstbasert visualisering (samme funksjon funker for a) og c))
def visualize_board(board: List[List[int]]):
    print("\nKnight's Tour – result (matrix):\n")
    print_board(board)
    print()

# --- Kjørbar del ---
if __name__ == "__main__":
    # a) vis tomt brett:
    print("Empty 8x8-brett:")
    print_board(make_empty_board())

    method = get_user_choice()
    start = (0, 0)  # evt. spør bruker: evaluer input til (rad, kol)
    if method == "Las Vegas":
        success, board = KnightsTourLasVegas(start)
    else:
        success, board = KnightsTourBacktracking(start)

    visualize_board(board)
    print("The tour was completed!" if success else "The tour was interrupted – the knight is stuck.")
