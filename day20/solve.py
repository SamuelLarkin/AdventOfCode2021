#!/usr/bin/env  python3

from tools_matrix import (
        load,
        solve,
        )




if __name__ == '__main__':
    lookup, image = load()
    if False:
        lookup, image = load('test.txt')
        print(lookup)
        print(image)

    answer = solve(lookup, image, num_steps=2)
    assert answer == 5203, f"Wrong answer ({answer})"
    print(f"Answer: {answer}")

    answer = solve(lookup, image, num_steps=50)
    assert answer == 18_806, f"Wrong answer ({answer})"
    print(f"Answer: {answer}")
