#!/usr/bin/env  python3

from tools import (
        load,
        part2,
        )




if __name__ == '__main__':
    graph = load()
    #graph = load("test1.txt")
    print(graph)

    answer = part2(graph)
    assert answer == 155_477, "Wrong answer"
    print(f"Answer: {answer}")
