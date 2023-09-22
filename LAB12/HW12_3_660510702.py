#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW12_3
# 204111 Sec 002

def my_id():
    return "660510702"
    
def main():
    # assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    # print(print_board(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]))
    print(ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]))


def ms_mine_hint(n_row, n_col, b_list):
    d = dict()

    # สร้าง board
    board = []
    for i in range (n_row):
        board += [[0] * n_col]

    # ใส่ระเบิดลงใน board
    for B in b_list:
        a, b = B
        board[a][b] = -1

        # เพิ่มค่ารอบช่องที่มีระเบิด
        for i in range(a-1, a+2):
            for j in range(b-1, b+2):
                if 0 <= i < n_row and 0 <= j < n_col and board[i][j] != -1:
                    board[i][j] += 1

    # สร้าง Dictionary เพื่อเก็บผลลัพธ์
    for i in range(n_row):
        for j in range(n_col):
            if board[i][j] > 0:
                d[(i, j)] = board[i][j]

    # คืนค่า
    return d


def print_board(n_row, n_col, b_list):
    max_len = len(str(max(n_row, n_col)))
    pad = ' '
    board_str = []
    board_str += [pad + pad*(max_len) +
                  pad.join(map(lambda x: str(x).zfill(max_len), range(n_col)))]

    for i in range(n_row):
        for j in range(n_col):
            if j == 0:
                temp = str(i).zfill(max_len) + pad
            pad2 = ' ' * (max_len - 1)
            if (i, j) in b_list:
                temp += pad2 + 'B' + pad
            else:
                temp += pad2 + '.' + pad
        board_str += [temp.rstrip()]

    print('\n'.join(board_str))


if __name__ == "__main__":
    main()
