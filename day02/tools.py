from dataclasses import dataclass
from typing import (
        List,
        Tuple,
        )



@dataclass
class Move:
    direction: str
    distance: int



def load(filename :str = "input.txt"):
    with open(filename, mode='r', encoding="UTF-8") as data:
        data = map(str.strip, data)
        data = map(str.split, data)
        data = map(lambda a: Move(a[0], int(a[1])), data)
        data = list(data)

    return data



def execute(moves: List[Move]) -> Tuple[int, int]:
    position = (0, 0)
    for move in moves:
        if move.direction == "down":
            position = (position[0], position[1]+move.distance)
        elif move.direction == "up":
            position = (position[0], position[1]-move.distance)
        elif move.direction == "forward":
            position = (position[0]+move.distance, position[1])
        else:
            raise(f"{move.direction} is invalid")

    return position



def aim(moves: List[Move]) -> Tuple[int, int]:
    position = (0, 0)
    aim = 0
    for move in moves:
        if move.direction == "down":
            aim += move.distance
        elif move.direction == "up":
            aim -= move.distance
        elif move.direction == "forward":
            position = (
                    position[0] + move.distance,
                    position[1] + aim * move.distance,
                    )
        else:
            raise(f"{move.direction} is invalid")

    return position
