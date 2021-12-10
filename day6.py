#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day6.txt") as file:
        data = [line for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    fishes = list(map(int, filter(None, data[0].split(','))))
    print("number of initial fishes is {}".format(fishes))
    max_iteration = 80
    for day in range(1, max_iteration+1):
        new_fishes = []
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 6
                new_fishes.append(8)
            else:
                fishes[idx] -= 1
        fishes.extend(new_fishes)
    print("After {} day there are {} fishes".format(max_iteration, len(fishes)))


def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()




