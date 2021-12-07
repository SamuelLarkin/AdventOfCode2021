#!/usr/bin/env  python3

from tools import (
        part2,
        load,
        )





if __name__ == '__main__':
    data = load()
    answer = part2(data)
    assert answer == 102_245_489, "Wrong answer"
    print(f"Answer: {answer}")
