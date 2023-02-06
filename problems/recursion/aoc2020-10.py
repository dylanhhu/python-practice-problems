"""
Starter code for Advent of Code 2019 Day #10

You must implement functions part1 and part2
"""

import sys
import os


def part1(jolts: 'list[int]') -> int:
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - jolts (list of integers)

    Returns an integer
    """

    # Replace with your code
    num_1_jolt = 0
    num_3_jolt = 0

    jolts.sort()  # sort the list
    jolts.append(jolts[-1] + 3)

    first_diff = jolts[0] - 0
    if first_diff == 1:
        num_1_jolt += 1
    elif first_diff == 3:
        num_3_jolt += 1

    for i, jolt in enumerate(jolts[1:]):
        diff = jolt - jolts[i]

        # print(i, ' ', jolt, ' ', diff, ' ', num_1_jolt, ' ', num_3_jolt)

        if diff == 1:
            num_1_jolt += 1
        elif diff == 3:
            num_3_jolt += 1

    return num_1_jolt * num_3_jolt


def part2(jolts: 'list[int]') -> int:
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - jolts (list of integers)

    Returns an integer
    """

    # Your code goes here
    return None


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        jolts = [int(x) for x in f.read().split()]

    print(f"Part 1:", part1(jolts))
    print(f"Part 2:", part2(jolts))
