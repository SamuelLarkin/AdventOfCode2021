#!/usr/bin/env  python3

import sys

from tools import (
        load,
        part2,
        )





if __name__ == '__main__':
    data = load()
    if len(sys.argv) > 1:
        data = load("test.txt")
        data.draw(use_borders=False)
        print(data.dimensions)

    answer = part2(data)
    assert answer == 2872, "Wrong answer"
    print(f"Answer: {answer}")
