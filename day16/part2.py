#!/usr/bin/env  python3

import sys

from tools import (
        load,
        part2,
        )




if __name__ == '__main__':
    data = load()

    answer = part2(data)
    assert answer == 68_703_010_504, "Wrong answer"
    print(f"Answer: {answer}")
