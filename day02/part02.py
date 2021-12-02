#!/usr/bin/env  python3


from tools import (
        aim,
        load,
        )





if __name__ == '__main__':
    position = aim(load())
    answer = position[0] * position[1]

    assert answer == 1856459736, "Wrong answer"
    print(f"Answer: {answer}")
