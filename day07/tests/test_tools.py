import pytest

from ..tools import (
        best_fuel_consumption,
        )




@pytest.mark.parametrize(
        "data,expected_value",
        [
            ((16,1,2,0,4,2,7,1,2,14), 37),
            ]
        )
def test_part1(data, expected_value):
    assert best_fuel_consumption(data) == expected_value




@pytest.mark.parametrize(
        "data,expected_value",
        [
            ((16,1,2,0,4,2,7,1,2,14), 168),
            ]
        )
def test_part2(data, expected_value):
    assert best_fuel_consumption(data, cost_fn=lambda d: (d *(d+1)//2)) == expected_value
