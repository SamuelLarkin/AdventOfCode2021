#!/usr/bin/env  python3

from tools import (
        bin2dec,
        epsilon_from_gamma,
        gamma,
        load,
        )



if __name__ == '__main__':
    data = load()
    g = gamma(data)
    print(bin2dec(g), g)
    e = epsilon_from_gamma(g)
    print(bin2dec(e), e)

    answer = bin2dec(g) * bin2dec(e)
    assert answer == 738234, "Wrong answer"
    print(f"Answer: {answer}")
