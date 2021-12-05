from collections import Counter
from dataclasses import dataclass
from typing import (
        List,
        )



@dataclass
class Coordinate:
    x: int
    y: int



@dataclass
class Line:
    """
    """
    start: Coordinate
    end: Coordinate

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    def draw(self):
        """
        Generate all coordinates on this line.
        """
        if self.is_vertical:
            x = self.start.x
            for y in range(self.start.y, self.end.y+1):
                yield Coordinate(x, y)
        elif self.is_horizontal:
            y = self.start.y
            for x in range(self.start.x, self.end.x+1):
                yield Coordinate(x, y)
        else:
            assert abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y), f"{self}"
            x_sign = sign(self.start.x, self.end.x)
            y_sign = sign(self.start.y, self.end.y)
            x = range(self.start.x, self.end.x+x_sign, x_sign)
            y = range(self.start.y, self.end.y+y_sign, y_sign)
            yield from (Coordinate(a, b) for a, b in zip(x, y))



def sign(start: int, end: int) -> int:
    if start < end:
        return 1
    else:
        return -1



def load(filename: str = "input.txt") -> List[Line]:
    """
    """
    def helper():
        with open(filename, mode="r", encoding="UTF-8") as cin:
            cin = map(str.strip, cin)
            for line in cin:
                start, _, end = line.split()
                start = tuple(map(int, start.split(',')))
                end = tuple(map(int, end.split(',')))
                s = min(start, end)
                e = max(start, end)
                yield Line(Coordinate(*s), Coordinate(*e))

    return list(helper())



def solve(lines: List[Line], use_diagonal: bool = False) -> int:
    """
    """
    counter = Counter()
    for line in lines:
        if use_diagonal or line.is_horizontal or line.is_vertical:
            counter.update((c.x, c.y) for c in line.draw())
        else:
            print(f"Skipping {line}")

        if False:
            print('=============================')
            print(line)
            print(counter)
            grid = [ [0]*10 for _ in range(10) ]
            for p, c in counter.items():
                grid[p[1]][p[0]] = c
            print(*grid, sep="\n")

    multiple = filter(lambda c: c[1]>1, counter.items())
    multiple = list(multiple)
    print(*multiple, sep="\n")

    return len(multiple)
