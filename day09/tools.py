import numpy as np

from functools import reduce
from scipy.signal import convolve2d



def load(filename: str = "input.txt"):
    with open(filename, mode='r', encoding="UTF-8") as cin:
        cin = map(str.strip, cin)
        cin = map(list, cin)
        data = [ list(map(int, line)) for line in cin ]

    return np.asarray(data)


def lowest_point(data):
    """
    Returns a map of the lowest points.
    """
    up = np.zeros((3, 3))
    up[1,1] = 1
    up[0,1] = -1
    down = np.zeros((3, 3))
    down[1,1] = 1
    down[2,1] = -1
    left = np.zeros((3, 3))
    left[1,1] = 1
    left[1,0] = -1
    right = np.zeros((3, 3))
    right[1,1] = 1
    right[1,2] = -1

    #print(up, down, left, right, sep="\n")

    lowest = np.ones_like(data)
    for c in (up, down, left, right):
        #print()
        #print(data)
        #print(c)
        filtered = convolve2d(data, c, mode="same", fillvalue=100)
        #print(filtered, (filtered < 0).astype(int), sep="\n")
        lowest &= filtered < 0

    #print()
    #print(lowest)
    return lowest



def part1(data, lowest) -> int:
    """
    What is the sum of the risk levels of all low points on your heightmap?
    """
    return np.sum(np.multiply(data + 1, lowest))



def part2(data, lowest) -> int:
    """
    What do you get if you multiply together the sizes of the three largest basins?
    """
    def basin_size(x, y):
        visited = set()
        to_explore = set(((x, y),))
        while len(to_explore) > 0:
            to_explore_new = set()
            for a, b in to_explore:
                for c, d in ((0,1), (0,-1), (1,0), (-1,0)):
                    e = a + c
                    f = b + d
                    e = max(0, min(data.shape[0]-1, e))
                    f = max(0, min(data.shape[1]-1, f))
                    if data[e,f] != 9:
                        if (e,f) not in visited:
                            to_explore_new.add((e,f))
                            visited.add((e,f))

            to_explore = to_explore_new

        return visited

    basins = [ basin_size(x, y) for x, y in np.argwhere(lowest>0) ]
    largest = sorted(basins, key=len)[-3:]

    if False:
        print(*map(len, basins))
        print(*basins, sep="\n")
        print(largest)

    return reduce(lambda a, b: a*b, map(len, largest), 1)
