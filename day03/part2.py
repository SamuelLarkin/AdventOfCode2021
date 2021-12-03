#!/usr/bin/env  python3

from tools import (
        CO2_scrubber_rating,
        bin2dec,
        load,
        oxygen_generator_rating,
        )





if __name__ == '__main__':
    data = load()
    if False:
        data = """00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010"""
        data = data.split()
        data = [ list(map(int, l)) for l in data ]

    o = oxygen_generator_rating(data)
    c = CO2_scrubber_rating(data)

    #print(o, bin2dec(o))
    #print(c, bin2dec(c))

    answer = bin2dec(o) * bin2dec(c)
    assert answer == 3969126, "Wrong answer"
    print(f"Answer: {answer}")
