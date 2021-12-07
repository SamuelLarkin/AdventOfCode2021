#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    data = load()
    answer = part1(data)
    assert answer == 355_989, "Wrong answer"
    print(f"Answer: {answer}")
