def is_valid(puzzle, row, col, num):

    for x in range(9):
        if puzzle[row][x] == num:
            return False

    for x in range(9):
        if puzzle[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    return True

def sudoku(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if sudoku(puzzle):
                            return puzzle
                        puzzle[row][col] = 0
                return
    return puzzle