#!/usr/bin/env python3

import sys
import math

def solve():
    with open("inputs/day7.txt") as file:
        data = [line for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    crab_positions = list(map(int, filter(None, data[0].split(','))))
    sorted_crab_positions = sorted(crab_positions)
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
    crab_positions = list(map(int, filter(None, data[0].split(','))))
    def get_total_fuel_cost(max_aligned_pos, positions):
        min_total_cost = math.inf
        for aligned_pos in range(max_aligned_pos + 1):
            total_cost = 0
            for idx, pos in enumerate(positions):
                diff = abs(positions[idx] - aligned_pos)
                total_cost += (diff * (diff + 1)) // 2
            min_total_cost = min(min_total_cost, total_cost)
        return min_total_cost
    total_fuel_cost = 0
    avg_crab_position = round(sum(crab_positions) / len(crab_positions))
    # try all positions from 0 to max = avg_crab_position (inclusive) and find
    # the minimum of all of these
    total_fuel_cost = get_total_fuel_cost(avg_crab_position, crab_positions)
    print("The total fuel spent to align to a position is\
        {}".format(total_fuel_cost))

    return total_fuel_cost

if __name__ == '__main__':
    solve()




