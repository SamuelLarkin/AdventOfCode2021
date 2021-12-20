import functools
import numpy as np

from collections import Counter
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



#@functools.lru_cache(None)
def align_scanner(scanner1: Scanner, scanner2: Scanner, num_align_required: int = 12) -> Set:
    """
    Can we align 12 probes from those two scanners?
    """
    set1 = to_set(scanner1)
    for p1, p2 in product(scanner1, scanner2):
        c2 = p1 - p2
        set2 = to_set(scanner2 + c2)
        intersection = set1 & set2
        if len(intersection) >= num_align_required:
            return intersection

    return set()



def rotate_and_align(scanner1: Scanner, scanner2: Scanner, num_align_required: int = 12):
    for rotation1 in BASIC_ROTATION_MATRICES:
        scanner1 = scanner1 @ rotation1
        for rotation2 in BASIC_ROTATION_MATRICES:
            scanner2 = scanner2 @ rotation2
            alignment = align_scanner(scanner1, scanner2)
            if len(alignment) > num_align_required:
                print(rotation1, rotation2)



def rotate_and_align2(scanner1: Scanner, scanner2: Scanner, num_align_required: int = 12):
    # (#b1, #coords) @ (#perms, #coords, #coords) => (#perms, #b1, #coords)
    perm1 = scanner1 @ BASIC_ROTATION_MATRICES
    # (#b2, #coords) @ (#perms, #coords, #coords) => (#perms, #b2, #coords)
    perm2 = scanner2 @ BASIC_ROTATION_MATRICES

    perm1 = np.expand_dims(perm1, 1)
    perm1 = np.expand_dims(perm1, 3)
    perm2 = np.expand_dims(perm2, 0)
    perm2 = np.expand_dims(perm2, 2)

    # Offset scanner2
    #   (1,      #perm2, 1,   #b2, #coords) # scanner2
    # - (#perm1, 1,      #b1, 1,   #coords) # scanner1
    # = (#perm1, #perm2, #b1, #b2, #coords) # offset
    offset = perm2 - perm1

    p1, p2, b1, b2, c = offset.shape
    # (#perm1, #perm2, #b1*#b2, #coors)
    offset = np.reshape(offset, (p1, p2, b1*b2, c))

    # Finding if some coords are aligned.
    sum_ = np.matmul(offset, offset.transpose((0,1,3,2)))   # (#perm1, #perm2, #b1*#b2, #b1*#b2)
    norm_ = np.linalg.norm(offset, axis=3)   # (#perm1, #perm2, #b1*#b2, #b1*#b2)
    cos_sim = sum_ / np.outer(norm_, norm_)

    counts = np.sum(cos_sim >= 1., axis=-1)
    max_aligned = np.max(counts, axis=-1)

    return max_aligned



def part1(data: Sequence[Scanner]) -> int:
    """
    How many beacons are there?
    """
    pass






if __name__ == '__main__':
    if True:
        scanner1 = ("0,2", "4,1", "3,3", "7,7")
        scanner2 = ("-1,-1", "-5,0", "-2,1")
        scanner1 = to_scanner(scanner1)
        scanner2 = to_scanner(scanner2)

        scanner1 = np.expand_dims(scanner1, 0)
        scanner2 = np.expand_dims(scanner2, 1)

        offset = scanner2 - scanner1
        offset = np.reshape(offset, (-1, 2))
        print(offset)
        sum_ = offset @ offset.T
        norm_ = np.linalg.norm(offset, axis=1)
        cos_sim = sum_ / np.outer(norm_, norm_)
        print(cos_sim)
        counts = np.sum(cos_sim >= 1., axis=1)
        max_aligned = np.max(counts)
        a = 1
        counter = Counter( tuple(o) for o in offset.reshape((-1, 2)))
        print(counter)

    if True:
        scanners = load()
        rotate_and_align2(scanners[0], scanners[1])
