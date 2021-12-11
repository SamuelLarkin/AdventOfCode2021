#!/usr/bin/env  python3

from tools import (
        load,
        part2,
        )






if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    #print(data)

    answer = part2(data)
    assert answer == 400, "Wrong answer"
    print(f"Answer: {answer}")
