

def check_row(num):
    global sudoku
    casella = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudoku[num][i] in casella:
            casella.remove(sudoku[num][i])
        else:
            return False
    return True

def check_col(num):
    global sudoku
    casella = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudoku[i][num] in casella:
            casella.remove(sudoku[i][num])
        else:
            return False
    return True

def check_square(num):
    global sudoku
    casella = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            if sudoku[i + (num // 3) * 3][j + (num % 3) * 3] in casella:
                casella.remove(sudoku[i + (num // 3) * 3][j + (num % 3) * 3])
            else:
                return False
    return True

def possible_casella(x,y):
    global sudoku_possibile, sudoku
    casella = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sudoku[x][y] == 0:
        for i in range(1,10):
            if i in sudoku:
                casella.remove(i)

def possible_solutions(x,y):
    global sudoku_possibile, sudoku
    casella = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sudoku[x][y] == 0:
        for i in range(1,10):


sudoku = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],

    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],

    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [5, 6, 7, 8, 9, 1, 2, 3, 4]
]

sudoku_possibile = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],

    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],

    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []]
]

for i in range(9):
    if check_square(i):
        print("Casella", i, "e' valida")
    else:
        print("Casella", i, "e' invalida")

