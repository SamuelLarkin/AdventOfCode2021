from itertools import (
        count,
        )
from typing import (
        List,
        )



def load(filename: str = "input.txt") -> List[List[int]]:
    """
    """
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        cin = map(list, cin)
        data = list(cin)

    return data



def step(data: List[List[str]]):
    """
    """
    new_world_east = [ [ v for v in l ] for l in data ]
    # >
    for j, line in enumerate(data):
        for i, v in enumerate(line):
            n = (i+1)%len(line)
            if v == '>' and data[j][n] == '.':
                new_world_east[j][i] = '.'
                new_world_east[j][n] = '>'

    new_world_south = [ [ v for v in l ] for l in new_world_east ]
    # v
    for j, line in enumerate(new_world_east):
        for i, v in enumerate(line):
            n = (j+1)%len(new_world_east)
            if v == 'v' and new_world_east[n][i] == '.':
                new_world_south[j][i] = '.'
                new_world_south[n][i] = 'v'

    return new_world_south



def part1(data: List[List[int]]) -> int:
    """
    What is the first step on which no sea cucumbers move?
    """
    for s in count():
        new_world = step(data)
        if new_world == data:
            break
        data = new_world

    if False:
        print(s+1)
        print(*data, sep='\n')

    return s+1
