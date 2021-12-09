#!/usr/bin/env  python3

from tools import (
        load,
        lowest_point,
        part1,
        )





if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    #print(data)

    lowest = lowest_point(data)
    answer = part1(data, lowest)
    assert answer == 496, "Wrong answer"
    print(f"Answer: {answer}")
