#!/usr/bin/env  python3

from tools import (
        load,
        part1,
        )




if __name__ == '__main__':
    graph = load()
    #graph = load("test1.txt")
    print(graph)

    answer = part1(graph)
    assert answer == 5920, "Wrong answer"
    print(f"Answer: {answer}")
