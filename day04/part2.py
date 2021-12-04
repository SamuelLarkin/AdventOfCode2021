#!/usr/bin/env  python3

from tools import (
        load,
        play_to_lose,
        )





if __name__ == '__main__':
    draw, boards = load()
    #draw, boards = load("test.txt")

    d, others = play_to_lose(draw, boards)
    print(d, others)
    answer = d * sum(others)
    assert answer == 13_158, "Wrong answer"
    print(f"Answer: {answer}")
