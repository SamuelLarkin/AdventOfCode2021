#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    polymer, reactions = load()
    if False:
        polymer, reactions = load('test.txt')
        print(polymer)
        print(reactions)

    answer = part1(polymer, reactions)
    assert answer == 3095, "Wrong answer"
    print(f"Answer: {answer}")
