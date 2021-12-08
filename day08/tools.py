from dataclasses import dataclass
from itertools import chain
from typing import (
        Dict,
        FrozenSet,
        List,
        Tuple,
        )



@dataclass
class Reading:
    wires: Tuple[FrozenSet[str]]
    digits: Tuple[FrozenSet[int]]
    digit2wire: Tuple[str] = None
    wire2digit: Dict[str, int] = None

    def __post_init__(self):
        assert len(self.wires) == 10, f"Wrong number of wires {len(self.wires)} {self.wires}"
        assert len(self.digits) == 4, f"Wrong number of digits {len(self.digits)} {self.digits}"

        wire2digit: Dict[str, int] = dict()
        digit2wire: List[str] = [ None for _ in range(10) ]

        # These are the wire configurations that have a single solution.
        for w in self.wires:
            if len(w) == 2:
                wire2digit[w] = 1
                digit2wire[1] = w
            elif len(w) == 3:
                wire2digit[w] = 7
                digit2wire[7] = w
            elif len(w) == 4:
                wire2digit[w] = 4
                digit2wire[4] = w
            elif len(w) == 7:
                wire2digit[w] = 8
                digit2wire[8] = w
            else:
                pass

        # For the remaining wires/digits, we need to deduce their mapping.
        mask_1 = set(digit2wire[1])
        mask_4 = set(digit2wire[4])
        for w in self.wires:
            wset= set(w)
            if w in wire2digit:
                continue
            if len(w) == 5:
                if len(wset & mask_1) == 2:
                    """
                    A `3` has 5 segments and has exactly 2 segments in common with `1`.
                    """
                    digit2wire[3] = w
                    wire2digit[w] = 3
                elif len(wset & mask_4) == 2:
                    """
                    A `2` has 5 segments and has exactly 2 segments in common with `4`
                    """
                    digit2wire[2] = w
                    wire2digit[w] = 2
                elif len(wset & mask_4) == 3:
                    """
                    A `5` has 5 segments and has exactly 3 segments in common with `4`.
                    """
                    digit2wire[5] = w
                    wire2digit[w] = 5
                else:
                    rasise(f"Unknown length 5: {w}")
            elif len(w) == 6:
                if len(wset & mask_1) == 1:
                    """
                    A `6` has 6 segments and has exactly 1 segments in common with `1`.
                    """
                    digit2wire[6] = w
                    wire2digit[w] = 6
                elif len(wset & mask_4) == 4:
                    """
                    A `9` has 6 segments and has exactly 4 segments in common with `4`.
                    """
                    digit2wire[9] = w
                    wire2digit[w] = 9
                elif len(wset & mask_4) == 3:
                    """
                    A `0` has 6 segments and has exactly 3 segments in common with `4`.
                    """
                    digit2wire[0] = w
                    wire2digit[w] = 0
                else:
                    raise(f"Unknown length 6 {w}")
            else:
                raise(f"Unhandled value {w}")

        assert len(wire2digit.keys()) == 10
        self.wire2digit = wire2digit
        assert all(filter(lambda e: e is not None, digit2wire))
        self.digit2wire = tuple(digit2wire)


    @property
    def value(self):
        """
        Return the decimal value represented by the digits.
        """
        val = sum( self.wire2digit[v]*10**(3-i) for i, v in enumerate(self.digits))

        return val



def load(filename: str = "input.txt") -> Tuple[Reading]:
    """
    Load the puzzle's input data.
    """
    data = []
    with open(filename, mode="r", encoding="UTF-8") as cin:
        cin = map(str.strip, cin)
        for line in cin:
            wires, digits = line.split('|')
            wires = map(str.strip, wires.split())
            wires = map(frozenset, wires)
            digits = map(str.strip, digits.split())
            digits = map(frozenset, digits)
            data.append(Reading(tuple(wires), tuple(digits)))

    return tuple(data)



def count_1_4_7_8(data: Tuple[Reading]) -> int:
    """
    part1
    In the output values, how many times do digits 1, 4, 7, or 8 appear?
    """
    number_segments = set((2, 4, 3, 7))
    candidates = map(lambda r: r.digits, data)
    candidates = chain.from_iterable(candidates)
    candidates = filter(lambda r: len(r) in number_segments, candidates)

    return len(list(candidates))



def sum_digits(data: Tuple[Reading]) -> int:
    """
    part2
    What do you get if you add up all of the output values?
    """
    total = sum(map(lambda r: r.value, data))

    return total
