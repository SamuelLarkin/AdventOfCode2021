import pytest

from ..tools import (
        aggregate,
        play,
        )


@pytest.mark.parametrize(
        "data,num_days,expected_value",
        [
            ((3,4,3,1,2), 18, 26),
            ((3,4,3,1,2), 80, 5934),
            ((3,4,3,1,2), 256, 26_984_457_539),
            ]
        )
def test_play(data, num_days, expected_value):
    data = aggregate(data)
    assert play(data, num_days) == expected_value
