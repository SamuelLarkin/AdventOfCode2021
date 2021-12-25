# https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpu84cj/?utm_source=share&utm_medium=web2x&context=3

from itertools import (
        cycle,
        product,
        )
from typing import (
        Dict,
        Iterable,
        List,
        )


Registers = Dict[str, int]

# https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpuaphy/?utm_source=share&utm_medium=web2x&context=3
# Extracted using `for n in instruction.*; do sed -n '6p' < $n; done`
coefficient_p = ( 10, 12, 13, 13, 14, -2, 11, -15, -10, 10, -10, -4, -1, -1 )
# Extracted using `for n in instruction.*; do sed -n '16p' < $n; done`
coefficient_q = ( 0, 6, 4, 2, 9, 1, 10, 6, 4, 6, 3, 9, 15, 5 )
# Extracted using `for n in instruction.*; do sed -n '5p' < $n; done`
coefficient_dz = ( 1, 1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 26, 26, 26 )



def load(filename: str= "input.txt") -> List[str]:
    """
    """
    with open(filename, mode='r', encoding='UTF-8') as cin:
        data = map(str.strip, cin.readlines())

    return data



def parse(instructions: List[str], numbers: Iterable = cycle((9,8,7,6,5,4,3,2,1))) -> Registers:
    """
    """
    registers = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
            }
    numbers = iter(numbers)
    for instruction in instructions:
        if instruction.startswith('inp'):
            i, r = instruction.split()
            #print(registers.items())
            number = int(next(numbers))
            assert number != 0
            registers[r] = number
        else:
            i, a, b = instruction.split()
            try:
                r_value = int(b)
            except:
                r_value = registers[b]

            if i == 'add':
                registers[a] += r_value
            elif i == 'mul':
                registers[a] *= r_value
            elif i == 'div':
                assert r_value != 0
                registers[a] //= r_value
            elif i == 'mod':
                assert registers[a] >= 0
                assert r_value > 0
                registers[a] %= r_value
            elif i == 'eql':
                registers[a] = int(registers[a] == r_value)
            else:
                assert False

    return registers



def execute(numbers: Iterable, coefficient1: Iterable, coefficient2: Iterable):
    """
    w = current_input_number
    x
    y
    z = accumulator

    inp w

    mul x 0  x = 0
    add x z  x = z
    mod x 26  x %= 26   # Make sure it isn't bigger than 26 aka alphabet size?
    div z 1  # Is this a noop?

    >add x 10

    eql x w  is x = x == w
    eql x 0  is x = x != w
    mul y 0   y = 0
    add y 25  y = 25
    mul y x   y = 25 if x != w else y = 0
    add y 1   y = 26 if x != w else y = 1
    mul z y   shift one letter over or not??
    mul y 0   y = 0
    add y w   y = w

    >add y 0

    mul y x   y if x != w or 0
    add z y
    """
    x, y, z = 0, 0, 0
    for w, c1, c2 in zip(numbers, coefficient1, coefficient2):
        x = z   # mul x 0 & add x z
        x %= 26   # mod x 26
        x += B   # add x 10
        x = int(x == w)   # eql x w
        x = int(x == 0)   # eql x 0

        z /= A   # div z 1 # Is this a noop?  ANSWER no because it is either 1 or 26

        y = 25   # mul y 0 & add y 25
        # mul y x & add y 1
        z *= y   # mul z y
        y = w   # mul y 0 & add y w
        y += C   # add y 0
        y *= x   # mul y x  where x is either 1 or 0

        z += y   # add z y

    return z == 0



def part1(instructions: List[str]) -> int:
    """
    What is the largest model number accepted by MONAD?
    """
    numbers = product((9,8,7,6,5,4,3,2,1), repeat=14)
    #numbers = product((1,2,3,4,5,6,7,8,9), repeat=14)
    if False:
        for number in numbers:
            answer = parse(instructions, number)
            if answer['z'] == 0:
                break
    else:
        for number in numbers:
            answer = execute(number, coefficient1, coefficient2)
            if answer:
                break

    return ''.join(map(str, number)), answer





if __name__ == '__main__':
    parse(
            ( 'inp w', 'add z w', 'mod z 2', 'div w 2', 'add y w', 'mod y 2', 'div w 2', 'add x w', 'mod x 2', 'div w 2', 'mod w 2', ),
            (7,),
            )
    answer = execute((0,9,9,9,9,9,9,9,9,9,9,9,9,9), coefficient1, coefficient2)
