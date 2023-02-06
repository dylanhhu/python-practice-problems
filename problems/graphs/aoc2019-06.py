"""
Starter code for Advent of Code 2019 Day #6

You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(orbits: 'dict[str, str]') -> int:
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    count = 0

    for object in orbits.values():
        count += 1

        while object := orbits.get(object, False):
            count += 1

    return count


def part2(orbits: 'dict[str, str]') -> int:
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    adjacency: 'dict[str, set[str]]' = {}

    # Create undirected graph
    for satellite, object in orbits.items():
        if satellite not in adjacency:
            adjacency[satellite] = set(object)
        else:
            adjacency[satellite].add(object)
        
        if object not in adjacency:
            adjacency[object] = set(satellite)
        else:
            adjacency[object].add(satellite)

    visited = set()
    queue = []
    start = 'YOU'
    end = orbits['SAN']
    queue.append(start)

    return bfs(adjacency, visited, start, end, 0)


def bfs(adjacency, visited, curr, end, count):
    if curr == end:
        return count
    
    counts = []
    visited.add(curr)

    for neighbor in adjacency[curr]:
        if neighbor not in visited:
            if count := bfs(adjacency, visited, neighbor, end, count + 1):
                counts.append(count)
        
    return min(counts) if counts else None
    


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
        lines = f.read().strip().split("\n")
        objs = [line.split(")") for line in lines]
        orbits = {}
        for p1, p2 in objs:
            orbits[p2] = p1

    print(f"Part 1:", part1(orbits))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(orbits))
