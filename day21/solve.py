#!/usr/bin/env  python3

from tools import (
        Player,
        part2,
        play,
        )





if __name__ == '__main__':
    answer = play(Player(10), Player(3))
    print(f"Answer: {answer}")
    assert answer == 742_257, f"Wrong answer ({answer})"

    answer = part2(Player(10), Player(3), 21)
    print(f"Answer: {answer}")
    assert answer == 93_726_416_205_179, f"Wrong answer ({answer})"
