#!/usr/bin/env  python3

from tools import (
        load,
        part2,
        )





if __name__ == '__main__':
    numbers = load()
    answer = part2(numbers)
    assert answer == 4635, "Wrong answer ({answer})"
    print(f"Answer: {answer}")
