#!/usr/bin/env  python3

from tools import (
        count_1_4_7_8,
        load,
        )






if __name__ == '__main__':
    data = load()
    if False:
        print(*data, sep='\n')

    answer = count_1_4_7_8(data)
    assert answer == 294, "Wrong answer"
    print(f"Answer: {answer}")
