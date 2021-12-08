#!/usr/bin/env  python3

from tools import (
        load,
        sum_digits,
        )






if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    if False:
        print(*data, sep='\n')

    answer = sum_digits(data)
    assert answer == 973292, "Wrong answer"
    print(f"Answer: {answer}")
