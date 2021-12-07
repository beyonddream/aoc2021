#!/usr/bin/env python3

import sys

def solve():
    with open("inputs/day1.txt") as file:
        data = [int(line) for line in file]
        solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    total_increase = 0
    current_increase_bucket = 0
    previous_value = data[0]
    for x in data[1:]:
        if x > previous_value:
            current_increase_bucket += 1
        else:
            total_increase += current_increase_bucket
            current_increase_bucket = 0
        previous_value = x
    total_increase += current_increase_bucket

    print("Total number of times a depth measurement increases is {}".format(total_increase))

def solve_part_2(data):
    total_increase = 0
    current_increase_bucket = 0
    previous_values_sum = sum(data[:3])
    for idx, _ in enumerate(data):
        try:
            current_values_sum = data[idx+1] + data[idx+2] + data[idx+3]
            if current_values_sum > previous_values_sum:
                current_increase_bucket += 1
            else:
                total_increase += current_increase_bucket
                current_increase_bucket = 0
            previous_values_sum = current_values_sum
        except IndexError:
            pass
    total_increase += current_increase_bucket

    print("Total number of sums larger than the previous sum is {}".format(total_increase))

if __name__ == '__main__':
    solve()
