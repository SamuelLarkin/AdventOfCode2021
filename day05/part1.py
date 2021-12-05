#!/usr/bin/env  python3


from tools import (
        load,
        solve,
        )




if __name__ == '__main__':
    data = load()
    #data = load("test.txt")
    if False:
        print(len(data))
        print(*data, sep="\n")

    answer = solve(data)
    assert answer == 5_145, "Wrong answer"
    print(f"Answer: {answer}")
