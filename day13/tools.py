import numpy as np

from typing import (
        List,
        Set,
        Tuple,
        )



def load(filename: str = "input.txt") -> Tuple[Set[Tuple[int, int]], List[str]]:
    points = set()
    instructions = []
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        for line in cin:
            if line.startswith("fold"):
                instructions.append(line)
            elif ',' in line:
                coord = tuple(map(int, line.split(',')))
                points.add(coord)
            else:
                pass

    return points, instructions



def fold(points: Set[Tuple[int, int]], instruction: str) -> Set[Tuple[int, int]]:
    folded = set()
    axe = int(instruction.split('=')[1])
    if 'x' in instruction:
        for point in points:
            if point[0] < axe:
                folded.add(point)
            else:
                folded.add((2*axe - point[0], point[1]))
    elif 'y' in instruction:
        for point in points:
            if point[1] < axe:
                folded.add(point)
            else:
                folded.add((point[0], 2*axe - point[1]))
    else:
        assert False, f"Invalid fold instruction {instruction}"

    return folded



def display(points: Set[Tuple[int, int]]) -> None:
    mx = max(p[0] for p in points)
    my = max(p[1] for p in points)
    if False:
        grid = np.full((mx+1, my+1), False, dtype=bool)
        for p in points:
            grid[p] = True

        for line in grid.T:
            print(*("O" if dot else " " for dot in line), sep='')
    else:
        import board
        b = board.Board((mx+1, my+1))
        for p in points:
            b[p] = 'O'
        b.draw(use_borders=False)

        b = board.Board((mx+1, my+1))
        b.populate(
                ['#'] * len(points),
                coord_iterable=points,
                )
        b.draw(use_borders=False)



def part1(points: Set[Tuple[int, int]], instructions: List[str]) -> int:
    """
    How many dots are visible after completing just the first fold instruction on your transparent paper?
    """
    instruction = instructions[0]
    
    return len(fold(points, instruction))



def part2(points: Set[Tuple[int, int]], instructions: List[str]) -> int:
    """
    What code do you use to activate the infrared thermal imaging camera system?
    """
    folded = set(points)
    for instruction in instructions:
        folded = fold(folded, instruction)

    #print(sorted(folded))
    display(folded)
