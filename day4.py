#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day4.txt") as file:
        data = [line.strip() for line in file]
        draws = [int(d) for d in data[0].split(',')]
        solve_part_1(data, draws)
        solve_part_2(data, draws)

def solve_part_1(data, draws, allow_squid_win=False):
    no_cols, no_rows = 5, 5
    idx = 1
    boards = []
    while idx < len(data):
        # start of new board
        if data[idx] == '':
            board = []
            boards.append(board)
        else:
            board.append([[int(col), False] for col in data[idx].split(' ') if col != ''])
        idx += 1
    completed_boards = []
    last_board = None
    last_draw = -1
    for draw in draws:
        for board in boards:
            if board not in completed_boards:
                found = update_board(board, draw)
                if found == True:
                    last_board = board
                    last_draw = draw
                    completed_boards.append(board)
                    if not allow_squid_win:
                        break
        else:
            continue
        break
    print_answer(last_board, last_draw)

def update_board(board, draw):
   found = True
   for row in board:
        for col_idx, col in enumerate(row):
           if col[0] == draw:
               col[1] = True
               # check row for bingo
               for col in row:
                   if col[1] == False:
                       found = False
                       break

               if found == True:
                   return found

               found = True # reset flag

               # check col for bingo
               for row in board:
                   if row[col_idx][1] == False:
                       found = False
                       break
               return found
   return False


def print_answer(board, draw):
    sum_of_unmarked = 0
    for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                    if col[1] == False:
                        sum_of_unmarked += col[0]
    score = sum_of_unmarked * draw
    print("Final score be if you choose that board {}, draw {}, sum_of_unmarked {} is {}".format(board, draw,
                                                          sum_of_unmarked,
                                                          score))

def solve_part_2(data, draws):
    solve_part_1(data, draws, True)

if __name__ == '__main__':
    solve()
