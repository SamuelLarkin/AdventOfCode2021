# Inspiration
# https://topaz.github.io/paste/#XQAAAQDMCQAAAAAAAAA6nMjJFHMADebh9lMSAXn5c0lZwzD7zOqDdANGvbGIFhrQhkIE+0Cjg0QZVCxSKOSjIX1zHaxyflUkyvN7sYCYdFnHxrXpeZpk1O5AFikQQipeyeFCyI7bxUgK7KxCAJm76itiv/sWAFgCRKUAA6XBT90h3regupMWZf4rpxKtDIUinq9c49j/vC2qGlw7U0YhgzN3T7O0jbdLTvX0a45v6nF0PDihjinW183q/KGeyrSU6ho82gkO+mje9jeDyxqVKoyQQ5e5MDspwJplAs/OBt+d0iKulQkUsqAuz59+w+VXT8hM3IayHR2zfxV8FySYYPyqPJ2/7fuIRCozJ7gJy997YdH9o2DD0ssZW2v/8NGScQkRBoTbAqD9xSTx0KqYA0zAYT7X827q3D9FBnuo4SaTgBilEYiBV9lhClMseKzBwALcsIG1yqo+CKmOTOT3dylSn2lCQ6h3kfxuK1/6xR1Vh7IvykGToeMwz5XKvcv2rA/oJABmBUhtiiIO1IQFJpCu4aFkgG+kR/vMt+V8pzIyJOHuJUYma6BUXYhgY3gvH/wvf6uH7roPIAU+zCdRvsWIy+m0ItDr0LINu299Pm+MVcKsgcsb5oFcdUM2K4SGE5GuRYOh2J4awYZKYUqVZ77ZdbtuT0EEKddW3n4krF9qRaVRMWurqMsZi1QtQS+FQZPMWi8j14IdznQZy5A75dADNx721n+x4g1OAo9uhSDM4fiIQ8MjevBdMgyLezg8uPOtENdoKTFmId7+QGeMMY3zEtGDdEP79tRhM4zcnldoGkazlzkw4jlN9UkV5lldqMwd8bmftQPfsWi0wWO7if6gIqfG1ztAZpf0PZn+b/Qv444FQgsSm6brR2r2mOWde9+1pO7MQL+Htt3zT/3jnfL0ckrrHu6O8tr55HbsDQPg78OGipippQA6C31i5XDdlaCo7K+lmNMN8/VzQ1Z0alHQ7YwS7yaFw2UljDrpkUUdVqnkB36JIScFsy7ZpJZTc9VnXPa+EXluZPnqSSN9n83LVQ5wYmxIFiUts1MLo3b9FV3At/CoqmR6bctaJB7I4KdINR3nOrXmwx0qUkogG45sB3aYddFZ/Q21erBdFaHzllGjHr9QA5LfmBw6K1q7ZFv5T6LhUyqfCP93dv599vGZKOzgkMKcTF9kQeuuaL7wx3ZklldHEfpW6bqJHCPnc4b/cKxyXeJ2Pir/3QQFNA==

import functools

from collections import (
        namedtuple,
        )
from itertools import permutations
from typing import (
        List,
        Sequence,
        )

Number = List

Value = namedtuple('Value', ('value', 'depth'))
Number = List[Value]



def load(filename: str = "input.txt") -> List[Number]:
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        cin = map(toSnailNumber, cin)
        return list(cin)



def toSnailNumber(line: str):
    def helper(line: str):
        depth = 0
        number = ''
        for c in line:
            if c == '[':
                depth += 1
            elif c == ']':
                if number != '':
                    yield Value(int(number), depth)
                    number = ''
                depth -= 1
            elif c == ',':
                if number != '':
                    yield Value(int(number), depth)
                    number = ''
                number = ''
            elif c == ' ':
                continue
            else:
                number += c
        if number != '':
            yield Value(int(number), depth)

    return list(helper(line))



def explode(number: Number) -> bool:
    """
    Retunrs if the Number was changed.
    To explode a pair, the pair's left value is added to the first regular
    number to the left of the exploding pair (if any), and the pair's right
    value is added to the first regular number to the right of the exploding
    pair (if any). Exploding pairs will always consist of two regular numbers.
    Then, the entire exploding pair is replaced with the regular number 0.
    """
    for i, v in enumerate(number):
        # before, v, w, after
        if v.depth == 5:
            # Right
            v = number.pop(i)
            w = number.pop(i)
            if i < len(number):
                after = number.pop(i)
                number.insert(i, Value(w.value+after.value, after.depth))

            number.insert(i, Value(0, v.depth-1))

            # left
            if i != 0:
                before = number.pop(i-1)
                number.insert(i-1, Value(before.value+v.value, before.depth))

            return True

    return False



def explode_not_finished(number: Number) -> Number:
    def helper(number: Number):
        previous = None
        # previous, v, w, x
        while len(number) > 0:
            v = number.pop(0)
            if v.depth == 4:
                # left
                if previous is None:
                    yield Value(0, v.depth-1)
                else:
                    yield Value(previous.value+v.value, previous.depth)

                w = number.pop(0)
                assert w.depth == 4
                # right
                if len(number) > 0:
                    x = number.pop(0)
                    yield Value(w.value+x.value, x.depth)
                else:
                    yield Value(0, w.depth-1)
                    
                # rest
                yield from number
            else:
                if previous is not None:
                    yield previous
            previous = v

    return list(helper(number))




def split(number: Number) -> Number:
    """
    If any regular number is 10 or greater, the leftmost such regular number splits.
    """
    for i, v in enumerate(number):
        if v.value >= 10:
            number.pop(i)
            a = v.value // 2
            b = v.value - a
            number.insert(i, Value(b, v.depth+1))
            number.insert(i, Value(a, v.depth+1))
            return True

    return False



def reduce(number: Number) -> Number:
    """
    To reduce a snailfish number, you must repeatedly do the first action in
    this list that applies to the snailfish number:

    - If any pair is nested inside four pairs, the leftmost such pair explodes.
    - If any regular number is 10 or greater, the leftmost such regular number splits.
    Once no action in the above list applies, the snailfish number is reduced.

    During reduction, at most one action applies, after which the process
    returns to the top of the list of actions. For example, if split produces a
    pair that meets the explode criteria, that pair explodes before other
    splits occur.
    """
    while explode(number) or split(number):
        pass

    return number



def add(a: Number, b: Number) -> Number:
    """
    Adds to numbers which increases the depth of each node.
    """
    return [ Value(n.value, n.depth+1) for n in a + b ]



def magnitude(number: Number) -> int:
    """
    Calculates the number's magnitude.
    """
    while len(number) > 1:
        for i, v in enumerate(number):
            if i+1<len(number) and v.depth == number[i+1].depth:
                v = number.pop(i)
                w = number.pop(i)
                number.insert(i, Value(3*v.value + 2*w.value, v.depth-1))
                break

    return number[0].value



def sum(numbers: Sequence[Number]) -> Number:
    """
    """
    result = functools.reduce(lambda a, b: reduce(add(a, b)), numbers)
    return result



def part2(numbers: Sequence[Number]) -> int:
    """
    What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
    """
    from tqdm import tqdm

    answer = 0
    pairs = permutations(numbers, 2)
    pairs = list(pairs)
    for a, b in tqdm(pairs):
        r = add(a, b)
        r = reduce(r)
        r = magnitude(r)
        answer = max(r, answer)

    return answer





if __name__ == '__main__':
    number_str = '[[[[[9,8],1],2],3],4]'
    number_str = '[7,[6,[5,[4,[3,2]]]]]'
    print(number_str)
    number = toSnailNumber(number_str)
    print(number)
    print(explode(number), number)
