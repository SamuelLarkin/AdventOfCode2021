#!/usr/bin/env  python3

from tools import (
        consecutive_diff,
        load,
        )



if __name__ == '__main__':
    answer = len(consecutive_diff(load()))

    assert answer == 1316, "Wrong answer"
    print(f"Answer: {answer}")
