# vim:nowrap

import pytest

from ..tools import (
        Cuboid,
        make_cuboid,
        split_cuboid,
        )
from typing import (
        List,
        Tuple,
        )




@pytest.mark.parametrize(
        "line,expected",
        (
            ('on x=10..12,y=10..12,z=10..12', Cuboid(((10,12),(10,12),(10,12)),1),),
        )
)
def test_make_range(line: str, expected: Cuboid):
    cuboid = make_cuboid(line)
    assert cuboid == expected



@pytest.mark.parametrize(
        "c1,c2,expected",
        (
            (
                Cuboid(((0,5),(0,1),(0,1)),1),
                Cuboid(((3,8),(0,1),(0,1)),0),
                (
                    Cuboid(((0,2),(0,0),(0,0)),1),
                    Cuboid(((6,8),(0,0),(0,0)),0),
                    Cuboid(((3,5),(0,0),(0,0)),0),
                    )),
            ),
)
def test_split(c1, c2, expected):
    answer = tuple(split_cuboid(c1, c2))
    assert answer == expected



def test_solve():
    data
