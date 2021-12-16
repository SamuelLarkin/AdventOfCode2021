import json

from functools import reduce
from typing import (
        List,
        )



def hex2bin(letter: str, scale: int = 16, num_of_bits: int = 4) -> str:
    """
    Convert letter to its binary representation.
    """
    return bin(int(letter, scale))[2:].zfill(num_of_bits)


def bin2int(code: str) -> int:
    """
    Convert a binary string to a integer
    """
    total = 0
    for i, b in enumerate(code[::-1]):
        b = 1 if b == '1' else 0
        total += b * 2**i

    return total


def load(filename: str = "input.txt") -> str:
    """
    """
    with open(filename, mode='r', encoding='UTF-8') as cin:
        line = cin.readline().strip()
        return line



class Stream:
    """
    Simply read from the data/stream.
    """
    def __init__(self, data: str):
        self.data = ''.join(map(hex2bin, data))
        self.index = 0

    def read_x_bits(self, x: int):
        value = self.data[self.index: self.index+x]
        self.index += x
        return bin2int(value)

    def read_multibytes(self):
        value = ''
        while self.data[self.index] == '1':
            value += self.data[self.index+1:self.index+5]
            self.index += 5
        value += self.data[self.index+1:self.index+5]
        self.index += 5
        value = bin2int(value)
        return value



def parse_version(data: Stream):
    """
    """
    assert False, "We have a better way of doing this with parse()"
    version = data.read_x_bits(3)
    yield version

    type_id = data.read_x_bits(3)

    if type_id == 4:
        # literal value
        value = data.read_multibytes()
    else:
        # operator
        length_type_id = data.read_x_bits(1)
        if length_type_id == 0:
            length = data.read_x_bits(15)
            current_index = data.index
            while data.index < current_index + length:
                yield from parse_packet(data)
            assert data.index == current_index + length, "Parse error length_type_id(0)"
        else:
            number_of_subpackets = data.read_x_bits(11)
            values = []
            for _ in range(number_of_subpackets):
                #values.append(data.read_x_bits(11))
                yield from parse_packet(data)



class Expression:
    def __init__(self, version, type_id, values):
        self.version = version
        self.type_id = type_id
        self.values  = values



class Literal(Expression):
    def __init__(self, version, type_id, values):
        # NOTE we set values to [] since a Literal has only a single value and
        # it also makes it easier to walk the tree for the expression's
        # version.
        super().__init__(version, type_id, [])
        self._value = values[0]

    def json(self):
        return {
                "Literal": self.value
                }

    @property
    def value(self):
        return self._value



class Sum(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Sum": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        return sum(v.value for v in self.values)



class Product(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Product": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        return reduce(lambda a, v: a * v.value, self.values, 1)



class Minimum(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Minimum": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        return min(v.value for v in self.values)



class Maximum(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Maximum": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        return max(v.value for v in self.values)



class Greater(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Greater": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        assert len(self.values) == 2
        return int(self.values[0].value > self.values[1].value)



class Less(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Less": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        assert len(self.values) == 2
        return int(self.values[0].value < self.values[1].value)



class Equal(Expression):
    def __init__(self, version, type_id, values):
        super().__init__(version, type_id, values)

    def json(self):
        return {
                "Equal": [ e.json() for e in self.values ]
                }

    @property
    def value(self):
        assert len(self.values) == 2
        return int(self.values[0].value == self.values[1].value)




def parse(data: Stream):
    """
    """
    version = data.read_x_bits(3)

    type_id = data.read_x_bits(3)

    if type_id == 4:
        # literal value
        value = data.read_multibytes()
        return Literal(version, type_id, values=[value])
    else:
        # operator
        length_type_id = data.read_x_bits(1)
        if length_type_id == 0:
            length = data.read_x_bits(15)
            current_index = data.index
            values = []
            while data.index < current_index + length:
                values.append(parse(data))
            assert data.index == current_index + length, "Parse error length_type_id(0)"
        else:
            number_of_subpackets = data.read_x_bits(11)
            values = [ parse(data) for _ in range(number_of_subpackets) ]

        if type_id == 0:
            return Sum(version, type_id, values)
        elif type_id == 1:
            return Product(version, type_id, values)
        elif type_id == 2:
            return Minimum(version, type_id, values)
        elif type_id == 3:
            return Maximum(version, type_id, values)
        elif type_id == 5:
            return Greater(version, type_id, values)
        elif type_id == 6:
            return Less(version, type_id, values)
        elif type_id == 7:
            return Equal(version, type_id, values)
        else:
            assert False, "Unknown type id {type_id}"



def version(expression: Expression):
    """
    Walk the expression tree and yield each Expression's version.
    """
    yield expression.version
    for e in expression.values:
        yield from version(e)



def part1(data: str) -> int:
    """
    Add up all of the version numbers.
    """
    print(data)
    data = Stream(data)
    expression = parse(data)
    print(json.dumps(expression.json(), indent=2, ensure_ascii=False))
    versions = list(version(expression))
    answer = sum(versions)

    return answer



def part2(data: str) -> int:
    """
    What do you get if you evaluate the expression represented by your
    hexadecimal-encoded BITS transmission?
    """
    print(data)
    data = Stream(data)
    expression = parse(data)
    print(json.dumps(expression.json(), indent=2, ensure_ascii=False))

    return expression.value
