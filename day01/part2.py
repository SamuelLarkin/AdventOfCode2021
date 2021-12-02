#!/usr/bin/env  python3

from tools import (
        consecutive_diff,
        load,
        triplet_sum,
        )



if __name__ == '__main__':
    answer = len(consecutive_diff(triplet_sum(load())))

    assert answer == 1344, "Wrong answer"
    print(f"Answer: {answer}")
