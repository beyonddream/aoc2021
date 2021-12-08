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
        for col_idx, col in enumerate(row):
            if col == '0':
                rate_counter[col_idx][0] += 1
            elif col == '1':
                rate_counter[col_idx][1] += 1

    gamma_rate = ''.join(['0' if r[0] > r[1] else '1' for r in rate_counter])
    epsilon_rate = ''.join(['1' if r[0] > r[1] else '0' for r in rate_counter])

    print("gamma_rate is {}, epsilon_rate is {}".format(gamma_rate, epsilon_rate))
    print("The power consumption of submarine is {}".format(int(gamma_rate, 2)
                                                            * int(epsilon_rate, 2)))
    return (gamma_rate, epsilon_rate)


def solve_part_2(data):
    o2_gen_rating, co2_scrub_rating = '', ''
    no_of_binary_cols = len(data[0].strip())
    o2_counter = [[0, 0] for col in range(no_of_binary_cols)]
    co2_counter = [[0, 0] for col in range(no_of_binary_cols)]
    col_idx = 0
    o2_data = data
    co2_data = data
    while col_idx < no_of_binary_cols:
        new_o2_data, new_co2_data = [], []
        if len(o2_data) > 1:
            for row in o2_data:
                if row[col_idx] == '0':
                    o2_counter[col_idx][0] += 1
                elif row[col_idx] == '1':
                    o2_counter[col_idx][1] += 1
            o2_selected_char = '1' if o2_counter[col_idx][1] >= o2_counter[col_idx][0] else '0'
            o2_gen_rating += o2_selected_char
            for row in o2_data:
                if row[col_idx] == o2_selected_char:
                    new_o2_data.append(row)
            o2_data = new_o2_data
            if len(o2_data) == 1:
                o2_gen_rating += o2_data[0][col_idx+1:].strip()
        if len(co2_data) > 1:
            for row in co2_data:
                if row[col_idx] == '0':
                    co2_counter[col_idx][0] += 1
                elif row[col_idx] == '1':
                    co2_counter[col_idx][1] += 1
            co2_selected_char = '0' if co2_counter[col_idx][0] <= co2_counter[col_idx][1] else '1'
            co2_scrub_rating += co2_selected_char
            for row in co2_data:
                if row[col_idx] == co2_selected_char:
                    new_co2_data.append(row)
            co2_data = new_co2_data
            if len(co2_data) == 1:
                co2_scrub_rating += co2_data[0][col_idx+1:].strip()

        col_idx += 1

    print("o2 selected is {}, co2 selected is {}".format(o2_gen_rating, co2_scrub_rating))
    print("Life support rating of the submarine is {}".format(int(o2_gen_rating,2) * int(co2_scrub_rating, 2)))


if __name__ == '__main__':
    solve()




