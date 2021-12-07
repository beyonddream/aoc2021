#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day2.txt") as file:
        data = [line.split(' ') for line in file]
        data = [[x[0], int(x[1])] for x in data]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    horizontal = 0
    depth = 0
    for x in data:
        if x[0] == 'forward':
            horizontal += x[1]
        elif x[0] == 'down':
            depth += x[1]
        elif x[0] == 'up':
            depth -= x[1]
    print("final answer multiplying horizontal {} and depth {} is {}".format(horizontal, depth, (horizontal*depth)))

def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()
