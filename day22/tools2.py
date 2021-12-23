# [Inspiration](https://pastebin.com/DbAVS7gz)
"""
Is this a game of venn graphs?
Are we trying to calculate intersection and union in 3d space?
"""
import copy
import re

from dataclasses import dataclass
from more_itertools import (
        chunked,
        )
from typing import (
        Iterable,
        Tuple,
        )



@dataclass(frozen=True)
class Range:
    min: int
    max: int

    @property
    def length(self):
        return self.max - self.min +1



@dataclass(frozen=True)
class Cuboid:
    """
    """
    x: Range
    y: Range
    z: Range
    state: int

    def __post_init__(self):
        assert self.x.min <= self.x.max
        assert self.y.min <= self.y.max
        assert self.z.min <= self.z.max

    @property
    def size(self):
        return self.x.length * self.y.length * self.z.length

    def intersect(self, other):
        if not ( self.x.min <= other.x.max and self.x.max >= other.x.min ):
            return False

        if not ( self.y.min <= other.y.max and self.y.max >= other.y.min ):
            return False

        if not ( self.z.min <= other.z.max and self.z.max >= other.z.min ):
            return False

        return True

    def intersection(self, other):
        x_min = max(self.x.min, other.x.min)
        x_max = min(self.x.max, other.x.max)

        y_min = max(self.y.min, other.y.min)
        y_max = min(self.y.max, other.y.max)

        z_min = max(self.z.min, other.z.min)
        z_max = min(self.z.max, other.z.max)

        state = self.state * other.state

        if self.state == other.state:
            state = -self.state
        elif self.state == 1 and other.state == -1:
            state = 1

        return Cuboid(
                Range(x_min, x_max),
                Range(y_min, y_max),
                Range(z_min, z_max),
                state,
                )



def make_cuboid(line: str) -> Cuboid:
    """
    """
    #on x=-27..27,y=-41..4,z=-9..38
    value_re = re.compile(r"([0-9-]+)")
    state, ranges = line.split()
    if state == 'on':
        state = 1
    elif state == 'off':
        state = -1
    else:
        assert False, f"Should be either on or off not {state}"

    coords = map(int, value_re.findall(ranges))
    ranges = map(lambda c: Range(*c), chunked(coords, 2))
    return Cuboid(*ranges, state)



def load(filename: str = "input.txt") -> Tuple[Cuboid]:
    """
    """
    #on x=-27..27,y=-41..4,z=-9..38
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        cuboids = [ make_cuboid(line) for line in cin ]

    return tuple(cuboids)



def solve(cuboids: Iterable) -> int:
    """
    """
    world = []
    for cuboid in cuboids:
        intersections = []
        for other in world:
            assert other.intersect(cuboid) == cuboid.intersect(other)
            if other.intersect(cuboid):
                # TODO: If this isn't symetrical, this strongly suggests we are
                # doing a diff like operation and not an intersection.
                #assert other.intersection(cuboid) == cuboid.intersection(other)
                intersections.append(cuboid.intersection(other))
        world.extend(intersections)
        if cuboid.state == 1:
            world.append(cuboid)
        #print()
        #print(*world, sep='\n')

    #print(*(c.size for c in world))
    answer = sum(c.state * c.size for c in world)
    return answer



def part1(cuboids: Tuple) -> int:
    """
    How many cubes are on?
    """
    def keep(cuboid: Cuboid) -> True:
        in_range = lambda c: -50 <= c <= 50
        ranges = (cuboid.x, cuboid.y, cuboid.z)
        return all(in_range(r.min) and in_range(r.max) for r in ranges)

    cuboids = list(filter(keep, cuboids))
    #print(len(cuboids))
    #print(*cuboids, sep='\n')

    return solve(cuboids)
