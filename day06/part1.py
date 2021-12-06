#!/usr/bin/env  python3

from tools import (
        load,
        play,
        )





if __name__ == '__main__':
    data = load()
    answer = play(data, days=80)
    assert answer == 389_726, "Wrong answer"
    print(f"Answer: {answer}")
