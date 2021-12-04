from dataclasses import dataclass
from itertools import chain
from more_itertools import partition
from typing import (
        List,
        Tuple,
        )


@dataclass
class Spot:
    """
    A square on a bingo card.
    """
    value: int   # Numerical value of the square
    checked: bool = False   # Was this number drawn

    def __str__(self):
        return f"+{self.value:2}" if self.checked else f" {self.value:2}"



class Board:
    """
    A bingo card which is a square of Spots.
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self._active = True

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    def __str__(self):
        representation = "\n".join(
                " ".join(str(s) for s in line)
                for line in self.grid
                )
        return representation

    def is_winner(self) -> bool:
        """
        A winning card has either a row of 5 spots that are checked or a line of spots that are checked.
        """
        for line in self.grid:
            if all(s.checked for s in line):
                return True
        for line in zip(*self.grid):
            if all(s.checked for s in line):
                return True
        return False

    def check(self, value: int):
        """
        Check the value on this bingo card.
        """
        for line in self.grid:
            for s in line:
                if s.value == value:
                    s.checked = True
                    return

    def bipartite(self) -> Tuple[List[int], List[int]]:
        """
        Return two lists, the first one is the winning numbers and the second one is the rest.
        """
        winners, others =  partition(lambda s: not s.checked, chain.from_iterable(self.grid))
        return list(winners), list(others)



def load(filename: str = "input.txt") -> Tuple[Tuple[int], List[Board]]:
    """
    Reads and parses the puzzle's input data into their representation.
    """
    with open(filename, mode="r", encoding="UTF-8") as cin:
        draw = cin.readline().strip().split(",")
        draw = list(map(int, draw))

        cin.readline()   # empty line

        boards = []
        board = []
        cin = map(str.strip, cin)
        for line in cin:
            if line == "":
                boards.append(Board(board))
                board = []
                continue
            line = map(int, line.split())
            line = map(Spot, line)
            line = list(line)
            board.append(line)

        boards.append(Board(board))

    return tuple(draw), boards



def play_to_win(draw: List[int], boards: List[Board]) -> Tuple[int, List[int]]:
    """
    Play until we get the first winning bingo card.
    """
    for d in draw:
        print("====================")
        print(d)
        for board in boards:
            board.check(d)
            print(board)
            print()
            if board.is_winner():
                marked, others = board.bipartite()
                print("Winner:", d, others)
                return d, [ s.value for s in others ]



def play_to_lose(draw: List[int], boards: List[Board]) -> Tuple[int, List[int]]:
    """
    Play until we get the last winning bingo card.
    """
    number_active = len(boards)
    for d in draw:
        print("====================")
        print(d)
        for board in boards:
            if not board.active:
                continue
            board.check(d)
            print(board)
            print()
            if board.is_winner():
                number_active -= 1
                board.active = False
            if number_active == 0:
                marked, others = board.bipartite()
                print("Winner:", d, others)
                return d, [ s.value for s in others ]
