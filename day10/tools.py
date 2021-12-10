from functools import reduce 
from typing import (
        Tuple,
        )



def load(filename: str = "input.txt") -> Tuple[str]:
    with open(filename, mode="r", encoding="UTF-8") as cin:
        data = tuple(map(str.strip, cin.readlines()))

    return data



points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        }



def illegal(data: str) -> int:
    """
    Return a score for the line.
    """
    stack = []
    for i, c in enumerate(data):
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            matching = stack[-1]
            if matching == '(' and c == ')' \
                    or matching == '[' and c == ']' \
                    or matching == '{' and c == '}' \
                    or matching == '<' and c == '>':
                if len(stack) == 0:
                    raise("Error, stack is empty!")
                stack.pop()
            else:
                return points[c]
    return 0



incomplete_points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
        }



def incomplete(data: str) -> int:
    """
    Return a score for the line.
    """
    stack = []
    for i, c in enumerate(data):
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            assert len(stack) > 0, "Error, stack is empty!"
            matching = stack.pop()
            if matching == '(' and c == ')' \
                    or matching == '[' and c == ']' \
                    or matching == '{' and c == '}' \
                    or matching == '<' and c == '>':
                continue
            else:
                assert False, "You need to filter the syntax error first."

    stack.reverse()

    return reduce(lambda a, c: 5*a+incomplete_points[c], stack, 0)



def part1(data: Tuple[str]) -> int:
    """
    What is the total syntax error score for those errors?
    """
    score = sum(illegal(l) for l in data)

    return score



def part2(data: Tuple[int]) -> int:
    """
    What is the middle score?
    """
    data = tuple(filter(lambda e: illegal(e) == 0, data))
    data = [ incomplete(d) for d in data ]
    data = sorted(data)
    #print(data)

    return data[len(data) // 2]
