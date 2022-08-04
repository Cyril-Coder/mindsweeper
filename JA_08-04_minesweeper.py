# TODO: start grid (uncovered grid) + timer + score
import random

# Generate the board 
def generateGrid(board, height, width, mines_total):

    # Empty board with all 0
    for x in range(width):
        row = []
        for y in range(height):
            row.append(0)
        board.append(row)
    
    # Add random mines to board
    while mines_total > sum(x.count('X') for x in board):
        # Generate a mines onto the board
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        board[y][x] = "X"

        # Add values adjacent to bomb
        # Note 2 things
        # -> (0,0) is top left of the board
        # -> y is rows, x is cols

        if (x >= 1 and x <= width-1) and (y >= 1 and y <= height-1):
            if board[y-1][x-1] != 'X':
                board[y-1][x-1] += 1 # Top left

        if (x >= 0 and x <= width-1) and (y >= 1 and y <= height-1):
            if board[y-1][x] != 'X':
                board[y-1][x] += 1  # Top middle

        if (x >= 0 and x <= width-2) and (y >= 1 and y <= height-1):
            if board[y-1][x+1] != 'X':
                board[y-1][x+1]+= 1 # Top right
                
        if (x >= 1 and x <= width-1) and (y >= 0 and y <= height-1):
            if board[y][x-1] != 'X':
                board[y][x-1] += 1 # Left

        if (x >= 0 and x <= width-2) and (y >= 0 and y <= height-1):
            if board[y][x+1] != 'X':
                board[y][x+1] += 1  # Right

        if (x >= 1 and x <= width-1) and (y >= 0 and y <= height-2):
            if board[y+1][x-1] != 'X':
                board[y+1][x-1] += 1 # Bottom left

        if (x >= 0 and x <= width-1) and (y >= 0 and y <= height-2):
            if board[y+1][x] != 'X':
                board[y+1][x] += 1 # Bottom middle

        if (x >=0 and x <= width-2) and (y >= 0 and y <= height-2):
            if board[y+1][x+1] != 'X':
                board[y+1][x+1] += 1 # Bottom right

    # Return generated board
    return board
    
# Set board and board size
board = []
# Beginner size is 9x9, intermediate is 16x16, expert is 30x16 
# Beginner has 10 mines, intermediate has 40, expert has 99 mines
height = 9
width = 9
mines_total = 10

# Call generateGrid with difficulty parameters
board = generateGrid(board, height, width, mines_total)

print(board)

# Print the board
for row in board:
    print(" | ".join(str(cell) for cell in row))