#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day7.txt") as file:
        data = [line for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    crab_positions = list(map(int, filter(None, data[0].split(','))))
    sorted_crab_positions = sorted(crab_positions)
    print("sorted crab positions = {}".format(sorted_crab_positions))
    no_of_crabs = len(sorted_crab_positions)
    def get_total_fuel_cost(aligned_pos_idx, positions):
        total_cost = 0
        for idx, pos in enumerate(positions):
            total_cost += abs(positions[idx] - positions[aligned_pos_idx])
        return total_cost
    total_fuel_cost = 0
    if no_of_crabs % 2 == 0:
        mid = no_of_crabs // 2
        total_fuel_cost = min(get_total_fuel_cost(mid, sorted_crab_positions),
                   get_total_fuel_cost(mid - 1, sorted_crab_positions))
    else:
        mid = no_of_crabs // 2
        total_fuel_cost = get_total_fuel_cost(mid, sorted_crab_positions)
    print("The total fuel spent to align to a position is\
        {}".format(total_fuel_cost))

    return total_fuel_cost

def solve_part_2(data):
    pass

if __name__ == '__main__':
    solve()




