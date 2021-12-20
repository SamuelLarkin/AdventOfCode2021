import functools
import numpy as np

from collections import Counter
from dataclasses import dataclass
from itertools import product
from typing import (
        List,
        Sequence,
        Set,
        Tuple,
        )


#Scanner = List[Tuple[int,int,int]]
Scanner = np.array



def get_cos_sin(degree: int) -> Tuple[int,int]:
    """
    Retunrs cos(degree), sin(degree)
    """
    if degree == 0:
        return 1, 0
    elif degree == 90:
        return 0, 1
    elif degree == 180:
        return -1, 0
    elif degree == 270:
        return 0, -1
    else:
        assert False, f"Unsupported degree ({degree})"



def get_rotation_matrix_x(degree: int):
    cos, sin = get_cos_sin(degree)
    return np.asarray([
        [ 1, 0, 0 ],
        [ 0, cos, -sin ],
        [ 0, sin,  cos ],
        ])



def get_rotation_matrix_y(degree: int):
    cos, sin = get_cos_sin(degree)
    return np.asarray([
        [ cos, 0, sin ],
        [ 0, 1, 0 ],
        [ -sin, 0, cos ],
        ])



def get_rotation_matrix_z(degree: int):
    cos, sin = get_cos_sin(degree)
    return np.asarray([
        [cos, -sin, 0 ],
        [sin,  cos, 0 ],
        [ 0, 0, 1 ],
        ])



if True:
    BASIC_ROTATION_MATRICES = frozenset(
            tuple(map(tuple, get_rotation_matrix_x(x) @ get_rotation_matrix_y(y) @ get_rotation_matrix_z(z)))
            for x, y, z in product((0, 90, 180, 270), repeat=3)
            )
    BASIC_ROTATION_MATRICES = np.asarray([ a for a in BASIC_ROTATION_MATRICES])
    #print(len(BASIC_ROTATION_MATRICES))
    print(BASIC_ROTATION_MATRICES)
    print(BASIC_ROTATION_MATRICES.shape)
else:
    BASIC_ROTATION_MATRICES = [
            get_rotation_matrix_x(x) * get_rotation_matrix_y(y) * get_rotation_matrix_z(z)
            for x, y, z in product((0, 90, 180, 270), repeat=3)
            ]



def to_scanner(scanner: Sequence[str]) -> Scanner:
    """
    """
    scanner = map(lambda x: x.split(','), scanner)
    return np.asarray(list(scanner), dtype=int)



def load(filename: str = "input.txt") -> List[Scanner]:
    """
    """
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        scanners = []
        scanner_desc = []
        for line in cin:
            if line == '':
                scanners.append(to_scanner(scanner_desc))
                scanner_desc = []
            elif 'scanner' in line:
                continue
            else:
                scanner_desc.append(line)

        if len(scanner_desc) > 0:
                scanners.append(to_scanner(scanner_desc))

    return scanners



def to_set(scanner: Scanner) -> Set:
    """
    """
    return set(map(tuple, scanner))



@dataclass
class Beacon:
    num_match: int
    coords: np.array



@dataclass
class ScannerCache:
    rotations: List[Beacon]

    @property
    def num_match(self):
        return sum(b.num_match for b in self.rotations)



def solve(scanners: List[Scanner]) -> int:
    """
    How many beacons are there?
    """
    world = scanners.pop()
    world = Counter(tuple(c) for c in world)
    cache = [
            ScannerCache([Beacon(0, s @ rotation) for rotation in BASIC_ROTATION_MATRICES] )
            for s in scanners
            ]

    deltas = []
    while len(cache) > 0:
        cache = sorted(cache, key=lambda s: s.num_match, reverse=True)
        for i, scanner in enumerate(cache):
            go_next = False
            print(i, len(cache), len(world))
            scanner = sorted(scanner.rotations, key=lambda a: a.num_match, reverse=True)
            for r, beacons in enumerate(scanner):
                offsets = Counter(
                        tuple(np.asarray(a) - b) for a, b in product(world.keys(), beacons.coords)
                        )
                offset, count = offsets.most_common()[0]
                beacons.num_match = count
                if count >= 12:
                    deltas.append(np.asarray(offset))
                    cache.pop(i)
                    world.update(tuple(c + offset) for c in beacons.coords)
                    go_next = True
                    break
            if go_next:
                break

    fartest = max(np.sum(np.abs(a -b)) for a, b in product(deltas, repeat=2))

    return len(world.keys()), fartest
