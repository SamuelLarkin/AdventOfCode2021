import copy
import re

from collections import (
        namedtuple,
        )
from dataclasses import dataclass
from itertools import (
        chain,
        product,
        )
from more_itertools import (
        chunked,
        )
from typing import (
        Generator,
        Iterable,
        List,
        Tuple,
        )



#CuboidBase = namedtuple('CuboidBase', ('coords', 'state'))
Range = Tuple[int, int]
@dataclass(frozen=True)
class Cuboid:
    ranges: Tuple[Range]
    state: int

    def __post_init__(self):
        assert len(self.ranges) == 3, "A Cuboid should have exactly 3 ranges"
        assert self.ranges[0][0] <= self.ranges[0][1]
        assert self.ranges[1][0] <= self.ranges[1][1]
        assert self.ranges[2][0] <= self.ranges[2][1]

    @property
    def size(self):
        return (self.ranges[0][1] - self.ranges[0][0] + 1) \
        * (self.ranges[1][1] - self.ranges[1][0] + 1) \
        * (self.ranges[2][1] - self.ranges[2][0] + 1)

    def trim(self, axe:int, new_range: Tuple[int, int]):
        new_ranges = list(self.ranges)
        new_ranges[axe] = new_range
        return Cuboid(tuple(new_ranges), self.state)

    def clone(self):
        return copy.deepcopy(self)



def make_cuboid(line: str) -> Cuboid:
    """
    """
    value_re = re.compile(r"([0-9-]+)")
    def helper(x1, x2, y1, y2, z1, z2, state):
        yield from (
                ((x, y, z), state) for x, y, z in product(
                range(x1, x2+1),
                range(y1, y2+1),
                range(z1, z2+1)))
    state, ranges = line.split()
    if state == 'on':
        state = 1
    elif state == 'off':
        state = 0
    else:
        assert False, f"Should be either on or off not {state}"

    coords = map(int, value_re.findall(ranges))
    ranges = map(tuple, chunked(coords, 2))
    return Cuboid(tuple(ranges), state)



def load(filename: str = "input.txt") -> Tuple[Cuboid]:
    #on x=-27..27,y=-41..4,z=-9..38
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        cuboids = [ make_cuboid(line) for line in cin ]

    return cuboids



def intersect_cuboid(c1: Cuboid, c2: Cuboid) -> bool:
    """
    """
    def helper(a1, a2, b1, b2):
        if a1 <= b1:
            return a1 <= b1 <= a2
        else:
            return b1 <= a1 <= b2

    return helper(*c1.ranges[0], *c2.ranges[0]) \
            and helper(*c1.ranges[1], *c2.ranges[1]) \
            and helper(*c1.ranges[2], *c2.ranges[2])



def split_cuboid(a: Cuboid, b: Cuboid, axe: int = 0) -> Generator[Cuboid, None, None]:
    """
    """
    if axe == 3:
        assert a.ranges[0] == b.ranges[0]
        assert a.ranges[1] == b.ranges[1]
        assert a.ranges[2] == b.ranges[2]
        if a.state & b.state:
            yield a.clone()
    else:
        if b.ranges[axe][0] < a.ranges[axe][0]:
            a, b = b, a

        a1, a2 = a.ranges[axe]
        assert a1 <= a2
        b1, b2 = b.ranges[axe]
        assert b1 <= b2
        assert a1 <= b1

        if not intersect_cuboid(a, b):
            # Disjoint
            if a.state == 1:
                yield a.clone()
            if b.state == 1:
                yield b.clone()
        elif a1 <= b1 <= b2 <= a2:
            if a1 <= b1-1 and a.state == 1:
                yield a.trim(axe, (a1, b1 - 1)) 

            if b2+1 <= a2 and a.state == 1:
                yield a.trim(axe, (b2 + 1, a2))

            if b1 <= b2:
                yield from split_cuboid(a.trim(axe, (b1, b2)), b, axe+1)
        elif a1 <= b1 <= a2 <= b2:
            if a1 <= b1-1 and a.state == 1:
                yield a.trim(axe, (a1, b1 - 1))

            if a2+1 <= b2 and b.state == 1:
                yield b.trim(axe, (a2 + 1, b2))

            if b1<=a2:
                yield from split_cuboid(a.trim(axe, (b1, a2)), b.trim(axe, (b1, a2)), axe+1)
        else:
            assert False



def merge(cuboids: Iterable) -> int:
    """
    """
    cuboids = iter(cuboids)
    world = set()
    world.add(next(cuboids))
    for cuboid in cuboids:
        new_world = set()
        for w in world:
            new_world |= set(split_cuboid(w, cuboid))
        assert all(c.state == 1 for c in new_world)
        world = new_world
        if False:
            answer = sum(c.size for c in world)
            print(*sorted(world, key=lambda c: c.ranges), sep='\n')
            print(answer)

    answer = sum(c.size for c in world)
    return answer



def part1(cuboids: Tuple) -> int:
    """
    How many cubes are on?
    """
    def keep(cuboid: Cuboid) -> True:
        return all(-50 <= c <= 50 for c in chain.from_iterable(cuboid.ranges))
    cuboids = list(filter(keep, cuboids))
    print(len(cuboids))
    print(*cuboids, sep='\n')
    return merge(cuboids)
