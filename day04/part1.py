#!/usr/bin/env  python3

from tools import (
        load,
        play_to_win,
        )





if __name__ == '__main__':
    draw, boards = load()
    #draw, boards = load("test.txt")

    d, others = play_to_win(draw, boards)
    print(d, others)
    answer = d * sum(others)
    assert answer == 54_275, "Wrong answer"
    print(f"Answer: {answer}")
