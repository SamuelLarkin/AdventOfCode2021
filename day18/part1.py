#!/usr/bin/env  python3

from tools import (
        load,
        magnitude,
        sum,
        )




if __name__ == '__main__':
    numbers = load()
    answer = sum(numbers)
    answer = magnitude(answer)

    assert answer == 4207, "Wrong answer ({answer})"
    print(f"Answer: {answer}")
