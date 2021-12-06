#!/usr/bin/env  python3

from tools import (
        load,
        play,
        )





if __name__ == '__main__':
    data = load()
    answer = play(data, days=256)
    assert answer == 1_743_335_992_042, "Wrong answer"
    print(f"Answer: {answer}")
