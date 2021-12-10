#!/usr/bin/env python3

import sys

MAX_ITERATION = 256

def solve():
    with open("inputs/day6.txt") as file:
        data = [line for line in file]
        # WARNING: This will take forever for max_iteration = 256
        #solve_part_1(data)
        solve_part_2(data)

def solve_part_1(data):
    fishes = list(map(int, filter(None, data[0].split(','))))
    max_iteration = MAX_ITERATION
    for day in range(1, max_iteration+1):
        new_fishes = []
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 6
                new_fishes.append(8)
            else:
                fishes[idx] -= 1
        fishes.extend(new_fishes)
    print("After {} day there are {} fishes. fishes {}".format(max_iteration, len(fishes),
                                                   fishes))


def solve_part_2(data):
    timers = list(map(int, filter(None, data[0].split(','))))
    max_iteration = MAX_ITERATION
    # represent each of the fish into 9 buckets (0 to 8)
    internal_timer_bucket = [0] * 9
    for timer in timers:
        internal_timer_bucket[timer] += 1

    for day in range(1, max_iteration+1):
        new_fishes = 0
        if internal_timer_bucket[0] != 0:
            new_fishes = internal_timer_bucket[0]
        # first move the fishes
        max_timer = len(internal_timer_bucket)
        for idx in range(max_timer - 1):
            internal_timer_bucket[idx] = internal_timer_bucket[idx+1]
        # now move new_fishes to 8 and add to 6
        if new_fishes > 0:
            internal_timer_bucket[-1] = new_fishes
            internal_timer_bucket[6] += new_fishes
        else:
            internal_timer_bucket[-1] = 0

    print("After {} day there are {} fishes. fishes {}".format(max_iteration,
                                                    sum(internal_timer_bucket),
                                                              internal_timer_bucket))

if __name__ == '__main__':
    solve()




