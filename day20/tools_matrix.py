import numpy as np

from typing import (
        Generator,
        Tuple,
        )

Coord = Tuple[int, int]
Lookup = np.array
Image = np.array



def add_border(data: np.array, border: int):
    """
    """
    if border == 0:
        image = np.zeros((data.shape[0]+4, data.shape[1]+4), dtype=int)
    else:
        image = np.ones((data.shape[0]+4, data.shape[1]+4), dtype=int)
    image[2:-2, 2:-2] = data
    return image



def load(filename: str = "input.txt") -> Tuple[Lookup, Image]:
    def convert(c: str) -> int:
        return 1 if c == '#' else 0

    with open(filename, mode='r', encoding='UTF-8') as cin:
        lookup = cin.readline().strip()
        lookup = np.asarray(tuple(map(convert, lookup)), dtype=int)
        assert lookup.shape[0] == 512

        cin.readline()  # Empty line

        data = cin.readlines()
        data = map(str.strip, data)
        data = [ list(map(convert, l)) for l in data ]
        image = np.asarray(data, dtype=int)

    return lookup, image



def offset(x: int, y: int, image: Image) -> int:
    """
    Caluculate the offset into the lookup based on the neighbors.
    """
    bits = image[x-1:x+2, y-1:y+2].ravel().tolist()
    bits = bits[::-1]
    answer = sum( 2**i for i, b in enumerate(bits) if b == 1 )
    assert 0 <= answer < 512

    return answer




def evolve(lookup: Lookup, image: Image, num_steps: int=2) -> Image:
    """
    """
    for step in range(num_steps):
        image = add_border(image, step % 2)
        new_image = np.zeros_like(image, dtype=int)
        for y in range(1, image.shape[1]-1):
            for x in range(1, image.shape[0]-1):
                o = offset(x, y, image)
                new_image[x, y] = lookup[o]
        image = new_image[1:-1,1:-1]
        #print(image)

    return new_image



def solve(lookup: Lookup, image: Image, num_steps: int=2) -> int:
    """
    How many pixels are lit in the resulting image?
    """
    o = offset(2, 2, image)
    image = evolve(lookup, image, num_steps)
    answer = np.count_nonzero(image)
    return answer
