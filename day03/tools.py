from typing import (
        List,
        )



def load(filename : str = "input.txt") -> List[List[int]]:
    with open(filename, mode="r", encoding="UTF-8") as cin:
        cin = map(str.strip, cin)
        cin = map(list, cin)
        cin = map(lambda l: list(map(int, l)), cin)
        data = list(cin)

    return data



def bin2dec(data: List[int]) -> int:
    value = 0
    expo = 1
    for d in data[::-1]:
        value += expo * d
        expo *= 2

    return value



def gamma(data: List[List[int]]) -> List[int]:
    half = len(data) // 2
    g = [
            int(half <= sum(l)) for l in zip(*data)
            ]

    return g



def epsilon_from_gamma(gamma: List[int]) -> List[int]:
    return [ 1 - b for b in gamma ]



def oxygen_generator_rating(data: List[List[int]]) -> List[int]:
    for i in range(len(data[0])):
        _len = len(data)
        g = sum(l[i] for l in data)
        data = [ e for e in data if e[i] == int(g >= (_len-g)) ]
        if len(data) == 1:
            break

    return data[0]



def CO2_scrubber_rating(data: List[List[int]]) -> List[int]:
    for i in range(len(data[0])):
        _len = len(data)
        g = sum(l[i] for l in data)
        data = [ e for e in data if e[i] != int(g >= (_len-g)) ]
        if len(data) == 1:
            break

    return data[0]
