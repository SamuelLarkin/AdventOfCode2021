from itertools import (
        count,
        product,
        )
from typing import (
        Generator,
        Tuple,
        )



def hit(vx, vy, xtarget=(211,232), ytarget=(-124,-69)):
    """
    Simulate the trajectory at a given speed in x / speed in y.
    """
    x = 0
    y = 0
    ymax = -9999999
    for step in count():
        x += vx
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        y += vy
        vy -= 1
        ymax = max(y, ymax)
        if x > xtarget[1] or y < ytarget[0]:
            return None, None
        elif x >= xtarget[0] and y <= ytarget[1]:
            return step, ymax



def all_velocities(xtarget=(211,232), ytarget=(-124,-69)) -> Generator[Tuple[int, int], None, None]:
    """
    """
    max_range=max(max(xtarget), -min(ytarget)) + 1
    for vx, vy in product(range(0, max_range), range(min(ytarget), max_range)):
        step, height = hit(vx, vy, xtarget, ytarget)
        if step is not None:
            yield (vx, vy, step, height)



def part1(xtarget=(211,232), ytarget=(-124,-69)) -> int:
    """
    What is the highest height position it reaches on this trajectory?
    """
    max_height = -999999
    for vx, vy, step, height in all_velocities(xtarget, ytarget):
        if height is not None:
            max_height = max(height, max_height)
        print(vx, vy, step, height)

    return max_height



def part2(xtarget=(211,232), ytarget=(-124,-69)) -> int:
    """
    How many distinct initial velocity values cause the probe to be within the target area after any step?
    """
    velocities = list(all_velocities(xtarget, ytarget))
    print(*velocities, sep='\n')

    return len(velocities)
