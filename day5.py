#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day5.txt") as file:
        data = [line.strip().split(' -> ') for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    grid = [row[:] for row in [[0] * 1000] * 1000]
    for line in data:
        x1, y1 = line[0].split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = line[1].split(',')
        x2, y2 = int(x2), int(y2)
        if x1 == x2: # horizontal
            start_y, end_y = (y1, y2+1) if y1 <= y2 else (y2, y1+1)
            for y in range(start_y, end_y):
                grid[y][x1] += 1
        elif y1 == y2: # vertical
            start_x, end_x = (x1, x2+1) if x1 <= x2 else (x2, x1+1)
            for x in range(start_x, end_x):
                grid[y1][x] += 1
    total_overlap = 0
    for y in grid:
        for x in y:
            if x > 1:
                total_overlap += 1
    print("The number of points where at least two lines overlap is {}".format(total_overlap))


def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()
