#!/usr/bin/env  python3

from tools import (
        load,
        solve,
        )





if __name__ == '__main__':
    data = load()
    if False:
        print(len(data))
        print(*data, sep='\n')

    answer1, answer2 = solve(data)
    print(f"Answer1: {answer1}")
    print(f"Answer2: {answer2}")
    assert answer1 == 454, "Wrong answer ({answer1})"
    assert answer2 == 10813, f"Wrong answer ({answer2})"
