import pytest

from ..tools import (
        part1,
        )


@pytest.mark.parametrize(
        "bits,expected_version",
        [
            ('D2FE28', 6),
            ('38006F45291200', 9),
            ('EE00D40C823060', 14),
            ('8A004A801A8002F478', 16),
            ('620080001611562C8802118E34', 12),
            ('C0015000016115A2E0802F182340', 23),
            ('A0016C880162017C3686B18A3D4780', 31),
            ]
        )
def test_version(bits, expected_version):
    version = part1(bits)
    assert version == expected_version
