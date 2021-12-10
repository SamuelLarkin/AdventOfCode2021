#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    #print(*data, sep="\n")

    answer = part1(data)
    assert answer == 367_227, "Wrong answer"
    print(f"Answer {answer}")
