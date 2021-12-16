#!/usr/bin/env  python3

import sys

from tools import (
        load,
        part1,
        )




if __name__ == '__main__':
    data = load()

    answer = part1(data)
    assert answer == 871, "Wrong answer"
    print(f"Answer: {answer}")
