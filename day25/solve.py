#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    data = load()
    if False:
        data = load('test.txt')

    answer = part1(data)
    print(f"Part I answer: {answer}")
    assert answer == 563, f"Wrong answer ({answer})"
