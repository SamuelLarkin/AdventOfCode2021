import numpy as np

from itertools import count



def load(filename: str= "input.txt"):
    with open(filename, mode="r", encoding="UTF-8") as cin:
        cin = map(str.strip, cin)
        data = map(list, cin)
        data = list(data)
        data = np.asarray(data).astype(int)

    return data



def perform_step(data):
    """
    """
    # First, the energy level of each octopus increases by 1.
    data += 1

    # This process continues as long as new octopuses keep having their energy
    # level increased beyond 9.
    while np.count_nonzero(data > 9) > 0:
        flashed = np.argwhere(data > 9)
        for x, y in flashed:
            # This increases the energy level of all adjacent octopuses by 1,
            # including octopuses that are diagonally adjacent.
            data[
                    max(0, x-1):min(9, x+1)+1,
                    max(0, y-1):min(9, y+1)+1
                    ] += 1
            # An octopus can only flash at most once per step.
            data[x,y] = -100000

    # Finally, any octopus that flashed during this step has its energy level
    # set to 0, as it used all of its energy to flash.
    data[data < 0] = 0

    return data



def part1(data, num_steps=100) -> int:
    """
    How many total flashes are there after 100 steps?
    """
    total = 0
    for step in range(num_steps):
        data = perform_step(data)
        total += np.count_nonzero(data == 0)
        #print(f"Step {step+1}:", data, sep="\n")

    return total



def part2(data) -> int:
    """
    What is the first step during which all octopuses flash?
    """
    for step in count(1):
        data = perform_step(data)
        if np.all(data == 0):
            return step
