#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )






if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    #print(data)

    answer = part1(data, 100)
    assert answer == 1735, "Wrong answer"
    print(f"Answer: {answer}")
