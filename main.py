sudoku = []

def row_def(index):
    if index >= 0 and index < 9:
        row=1
    elif index >= 9 and index < 18:
        row=2
    elif index >= 18 and index < 27:
        row=3
    elif index >= 27 and index < 36:
        row=4
    elif index >= 36 and index < 45:
        row=5
    elif index >= 45 and index < 54:
        row=6
    elif index >= 54 and index < 63:
        row=7
    elif index >= 63 and index < 72:
        row=8
    elif index >= 72 and index < 81:
        row=9
    else:
        return -1
    return row

def col_def(index):
    if index // 9 == 0:
        col=1
    elif index // 9 == 1:
        col=2
    elif index // 9 == 2:
        col=3
    elif index // 9 == 3:
        col=4
    elif index // 9 == 4:
        col=5
    elif index // 9 == 5:
        col=6
    elif index // 9 == 6:
        col=7
    elif index // 9 == 7:
        col=8
    elif index // 9 == 8:
        col=9
    else:
        return -1
    return col

def check_row(index, num):
    for 


# indici corrispondendi alle caselle
# [
#   0,   1,  2,      3,  4,  5,      6,  7,  8,
#   9,  10, 11,     12, 13, 14,     15, 16, 17,
#   18, 19, 20,     21, 22, 23,     24, 25, 26,
#
#   27, 28, 29,     30, 31, 32,     33, 34, 35,
#   36, 37, 38,     39, 40, 41,     42, 43, 44,
#   45, 46, 47,     48, 49, 50,     51, 52, 53,
#
#   54, 55, 56,     57, 58, 59,     60, 61, 62,
#   63, 64, 65,     66, 67, 68,     69, 70, 71,
#   72, 73, 74,     75, 76, 77,     78, 79, 80
# ]

# costruisci il tuo sudoku
sudoku = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]
