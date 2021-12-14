from collections import Counter
from typing import (
        Dict,
        Tuple,
        )



def load(filename: str = "input.txt") -> Tuple[str, Dict[int, Tuple[str,str]]]:
    """
    """
    reactions = dict()
    with open(filename, mode='r', encoding='UTF-8') as cin:
        polymer = cin.readline().strip()
        cin.readline()
        cin = map(str.strip, cin)
        for line in cin:
            i, _, o = line.split()
            assert i not in reactions
            reactions[i] = (i[0]+o, o+i[1])

    return polymer, reactions



def polymerize_step(state: Dict[str, int], reactions: Dict[int, Tuple[str,str]]) -> Counter:
    """
    """
    new_state = Counter()
    for k, v in state.items():
        if k not in reactions:
            new_state.update({k, v})
        else:
            c1, c2 = reactions[k]
            new_state.update({
                c1: v,
                c2: v,
                })

    return new_state



def polymerize(polymer: str, reactions: Dict[int, Tuple[str,str]], num_steps: int = 10) -> Counter:
    """
    Performs the polymerisation of `polymer` with the `reactions`.
    """
    state = Counter([a+b for a, b in zip(polymer, polymer[1:])])
    print(state)

    for _ in range(num_steps):
        state = polymerize_step(state, reactions)

    return state



def solve(polymer: str, reactions: Dict[int, Tuple[str,str]], num_steps: int = 10) -> int:
    """
    What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    """
    state = polymerize(polymer, reactions, num_steps)
    alphabet = Counter(polymer[-1])
    for k, v in state.items():
        # Note that the second letter is the first letter of the next pair thus
        # if we count the second letter it will be counted twice.
        alphabet.update({
            k[0]: v,
            })
    print(alphabet)
    maximum = alphabet.most_common()[0][1]
    minimum = alphabet.most_common()[-1][1]

    return maximum - minimum



def part1(polymer: str, reactions: Dict[int, Tuple[str,str]]) -> int:
    """
    What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    For 10 steps.
    """
    return solve(polymer, reactions, 10)



def part2(polymer: str, reactions: Dict[int, Tuple[str,str]]) -> int:
    """
    What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    For 40 steps.
    """
    return solve(polymer, reactions, 40)
