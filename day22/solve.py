#!/usr/bin/env  python3

from tools2 import (
        load,
        part1,
        solve,
        )





if __name__ == '__main__':
    data = load()
    if False:
        #data = load('test.txt')
        #data = load('test_larger.txt')
        data = load('test_largest.txt')
        print(len(data))
        print(*data, '\n', sep='\n')

    # Part1
    answer = part1(data)
    print(f"Part I answer {answer}")
    assert answer == 587_785, f"Wrong answer ({answer})"

    # Part2
    answer = solve(data)
    print(f"Part II answer {answer}")
    assert answer == 1_167_985_679_908_143, f"Wrong answer ({answer})"
