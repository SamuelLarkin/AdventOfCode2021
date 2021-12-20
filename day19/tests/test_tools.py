import pytest

from ..tools import (
        align_scanner,
        load,
        rotate_and_align,
        rotate_and_align2,
        to_scanner,
        to_set,
        )


scanners = load('test.txt')



@pytest.mark.parametrize(
        "scanner1,scanner2,require_to_align",
        (
            (("0,2", "4,1", "3,3"), ("-1,-1", "-5,0", "-2,1"), 3),
            )
        )
def test_align_scanner(scanner1, scanner2, require_to_align):
    scanner1 = to_scanner(scanner1)
    scanner2 = to_scanner(scanner2)
    alignment = align_scanner(scanner1, scanner2, require_to_align)
    assert len(alignment) >= require_to_align



@pytest.mark.parametrize(
        "scanner1,scanner2,require_to_align,expected",
        (
            (scanners[0], scanners[1], 12, ( '-618,-824,-621', '-537,-823,-458', '-447,-329,318', '404,-588,-901', '544,-627,-890', '528,-643,409', '-661,-816,-575', '390,-675,-793', '423,-701,434', '-345,-311,381', '459,-707,401', '-485,-357,347',)),
            (scanners[1], scanners[0], 12, ( '686,422,578', '605,423,415', '515,917,-361', '-336,658,858', '-476,619,847', '-460,603,-452', '729,430,532', '-322,571,750', '-355,545,-477', '413,935,-424', '-391,539,-444', '553,889,-390',)),
            )
        )
def test1(scanner1, scanner2, require_to_align, expected):
    #expected = to_set(to_scanner(expected))
    alignment = rotate_and_align2(scanner1, scanner2, require_to_align)
    #print("EXPECTED", expected)
    #print("ALIGNMENT", alignment)
    #assert alignment == expected
    assert alignment >= require_to_align
