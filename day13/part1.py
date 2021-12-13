#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )





if __name__ == '__main__':
    points, instructions =  load()
    #points, instructions =  load("test.txt")
    #print(points, instructions)

    answer = part1(points, instructions)
    assert answer == 655, "Wrong answer"
    print(f"Answer: {answer}")
