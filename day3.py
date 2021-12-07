#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day3.txt") as file:
        data = [line for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    no_of_binary_cols = len(data[0].strip())
    rate_counter = [[0, 0] for col in range(no_of_binary_cols)]
    for row in data:
        row_str = str(row)
        for col_idx, col in enumerate(row_str):
            if col == '0':
                rate_counter[col_idx][0] += 1
            elif col == '1':
                rate_counter[col_idx][1] += 1

    gamma_rate = int(''.join(['0' if r[0] > r[1] else '1' for r in rate_counter]), 2)
    epsilon_rate = int(''.join(['1' if r[0] > r[1] else '0' for r in rate_counter]), 2)

    print("The power consumption of submarine is {}".format(gamma_rate * epsilon_rate))

def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()




