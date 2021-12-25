import pytest

from ..tools import (
        Registers,
        parse,
        )
from typing import (
        Iterable,
        List,
        )



def negates(number: int):
    """
    Here is an ALU program which takes an input number, negates it, and stores
    it in x.
    """
    return (
            ('inp x', 'mul x -1',),
            (number,),
            {'w': 0, 'x': -number, 'y': 0, 'z': 0},
            )



def is_three_times_larger(n1: int, n2: int, answer: bool):
    """
    Here is an ALU program which takes two input numbers, then sets z to 1 if
    the second input number is three times larger than the first input number,
    or sets z to 0 otherwise.
    """
    return (
            ( 'inp z', 'inp x', 'mul z 3', 'eql z x', ),
            (n1, n2),
            {'w': 0, 'x': n2, 'y': 0, 'z': int(answer)},
            )


def to_binary(number: int, answer: Registers):
    """
    Here is an ALU program which takes a non-negative integer as input,
    converts it into binary, and stores the lowest (1's) bit in z, the
    second-lowest (2's) bit in y, the third-lowest (4's) bit in x, and the
    fourth-lowest (8's) bit in w.
    """
    assert number >= 0
    return (
            ( 'inp w', 'add z w', 'mod z 2', 'div w 2', 'add y w', 'mod y 2', 'div w 2', 'add x w', 'mod x 2', 'div w 2', 'mod w 2', ),
            (number, ),
            answer,
            )




@pytest.mark.parametrize(
        "instuctions,numbers,expected",
        (
            negates(4),
            negates(-7),
            is_three_times_larger(1, 3, True),
            is_three_times_larger(2, 3, False),
            to_binary(7, {'w': 0, 'x': 1, 'y': 1, 'z': 1}),
            )
)
def test_parse(instuctions: List[str], numbers: Iterable, expected):
    print(instuctions, *numbers, expected)
    registers = parse(instuctions, numbers)
    print(registers)
    assert registers == expected
