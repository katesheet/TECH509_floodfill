from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    # print(input_board[x])
    # print(type(input_board[x]))
    # print(input_board[x][y])
    m = len(input_board) # m is the row number of the board
    n = len(input_board[0]) # n is the column number of the board

    if x >= 0 and x < m and y >= 0 and y < n:
        if input_board[x][y] == old:
            # input_board[x][y] = new
            # print(input_board)
            input_board[x] =  input_board[x][:y]+ new + input_board[x][y+1:]
            flood_fill(input_board = input_board, old = old, new = new, x = x-1, y = y)
            flood_fill(input_board = input_board, old = old, new = new, x = x+1, y = y)
            flood_fill(input_board = input_board, old = old, new = new, x = x, y = y-1)
            flood_fill(input_board = input_board, old = old, new = new, x = x, y = y+1)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###...............",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~##########~~~~~~
# ~~~~~~#~~~~~~~~#~~~~~~
# ~~~~~~#~~~~~~~~#~~~~~~
# ~~~~~~#~~~~~~~~#####~~
# ~~~~###~~~~~~~~~~~~~~~
# ~~~~#~~~~~~~~~~~~###~~
# ~~~~##############~~~~
