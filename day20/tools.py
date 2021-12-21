from board import Board
from collections import defaultdict
from typing import (
        Dict,
        Generator,
        List,
        Tuple,
        )

Coord = Tuple[int, int]
Lookup = Tuple[int]
Image = Dict[Coord, int]


def load(filename: str = "input.txt") -> Tuple[Lookup, Image]:
    def convert(c: str) -> int:
        return 1 if c == '#' else 0

    with open(filename, mode='r', encoding='UTF-8') as cin:
        lookup = cin.readline().strip()
        lookup = tuple(map(convert, lookup))
        assert len(lookup) == 512

        cin.readline()  # Empty line

        data = cin.readlines()
        data = map(str.strip, data)
        data = [ list(map(convert, l)) for l in data ]
        image = defaultdict(lambda: 0)
        for y, line in enumerate(data):
            for x, data in enumerate(line):
                image[(x,y)] = data

    # TODO add border to image.
    for a in range(-1, y+2):
        image[-1,  a] = 0
        image[x+1, a] = 0

    for a in range(-1, x+2):
        image[a,  -1] = 0
        image[a, y+1] = 0

    return lookup, image



def neighbors(x: int, y: int, image: Image) -> Generator[Coord, None, None]:
    """
    """
    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            yield x+i, y+j



def offset(x: int, y: int, image: Image) -> int:
    """
    Caluculate the offset into the lookup based on the neighbors.
    """
    n = list(neighbors(x, y, image))
    assert len(n) == 9
    answer = sum( 2**i for i, coords in enumerate(n[::-1]) if image[coords] == 1 )
    assert 0 <= answer < 512
    return answer




def evolve(lookup: Lookup, image: Image, num_steps: int=2) -> Image:
    """
    """
    if False:
        b = Board((110, 110))
        for (x, y), v in image.items():
            b[(x+1, y+1)] = v
        b.draw(use_borders=False)

    for step in range(num_steps):
        new_image = defaultdict(lambda: step % 2)
        for (x, y), v in list(image.items()):
            o = offset(x, y, image)
            new_image[(x, y)] = lookup[o]
        image = new_image

        if True:
            # Create the boarder in a super lazy way aka the most inefficient way ;)
            for x, y in list(image.keys()):
                for coords in list(neighbors(x, y, image)):
                    image[coords]

        if True:
            b = Board((110, 110))
            for (x, y), v in image.items():
                b[(x+step+2, y+step+2)] = v
            b.draw(use_borders=False)

    return image



def part1(lookup: Lookup, image: Image, num_steps: int=2) -> int:
    """
    How many pixels are lit in the resulting image?
    """
    image = evolve(lookup, image, num_steps)
    answer = filter(lambda x: x == 1, image.values())
    answer = list(answer)
    return len(answer)
