def main():
    '''
    it will be the main part of solving the sudoku
    '''
    '''main_sudo = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        [4, 5, 6, 7, 8, 9, 1, 2, 3]
        [7, 8, 9, 1, 2, 3, 4, 5, 6]
        [3, 1, 2, 6, 4, 5, 9, 7, 8]
        [6, 4, 5, 9, 7, 8, 3, 1, 2]
        [9, 7, 8, 3, 1, 2, 6, 4, 5]
        [2, 3, 1, 5, 6, 4, 8, 9, 7]
        [5, 6, 4, 8, 9, 7, 2, 3, 1]
        [8, 9, 7, 2, 3, 1, 5, 6, 4]
    ]'''        # its the answer dont look at it ;)
    main_sudo = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0]
    ]       # 0 mean that there is nothing
    # print(main_sudo)
    solve(main_sudo)
    print_board(main_sudo)

# solver.py

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

if __name__ == '__main__':
    main()