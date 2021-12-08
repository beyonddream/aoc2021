#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day4.txt") as file:
        data = [line.strip() for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    no_cols, no_rows = 5, 5
    draws = [int(d) for d in data[0].split(',')]
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
    for draw in draws:
        for board in boards:
            found = update_board(board, draw)
            if found == True:
                print_answer(board, draw)
                break
        else:
            continue
        break

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

def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()
