#!/usr/bin/env  python3


from tools import (
        execute,
        load,
        )





if __name__ == '__main__':
    position = execute(load())
    answer = position[0] * position[1]

    assert answer == 2039256, "Wrong answer"
    print(f"Answer: {answer}")
