#!/usr/bin/env  python3

import sys

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    data = load()
    if len(sys.argv) > 1:
        data = load("test.txt")
        data.draw(use_borders=False)
        print(data.dimensions)

    answer = part1(data)
    assert answer == 508, "Wrong answer"
    print(f"Answer: {answer}")
