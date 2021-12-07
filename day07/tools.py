from typing import (
        List,
        )



def load(filename: str = "input.txt") -> List[int]:
    with open(filename, mode="r", encoding="UTF-8") as cin:
        data = cin.readline()
        data = data.strip()
        data = data.split(',')
        data = list(map(int, data))

    return data



def best_fuel_consumption(data: List[int], cost_fn = lambda x: x) -> int:
    """
    """
    def helper(displacement_fn):
        best_consumption = 999999999
        best_position = None
        for d in range(maximum_distance):
            position = displacement_fn(average, d)
            # Position is out-of-bound
            if position < 0 or position >= maximum_distance:
                continue
            consumption = sum(cost_fn(abs(p-position)) for p in data)
            #print(f"position: {position} consumption: {consumption}")
            if best_consumption is None or consumption < best_consumption:
                best_consumption = consumption
                best_position = position
            else:
                break

        return best_consumption


    average = sum(data) // len(data)

    maximum_distance = max(data)
    #print(f"maximum_distance: {maximum_distance}")

    best_consumption = min(
            helper(lambda p, d: p+d),
            helper(lambda p, d: p-d),
                )
    if False:
        for d in range(maximum_distance):
            position = average + d
            # Position is out-of-bound
            if position < 0 or position >= maximum_distance:
                continue
            consumption = sum(cost_fn(abs(p-position)) for p in data)
            #print(f"consumption: {consumption}")
            if best_consumption is None or consumption < best_consumption:
                best_consumption = consumption
                best_position = position

            position = average - d
            # Position is out-of-bound
            if position < 0 or position >= maximum_distance:
                continue
            consumption = sum(cost_fn(abs(p-position)) for p in data)
            #print(f"consumption: {consumption}")
            if best_consumption is None or consumption < best_consumption:
                best_consumption = consumption
                best_position = position

    return best_consumption



def part1(data: List[int]) -> int:
    """
    How much fuel must they spend to align to that position?
    """
    return best_fuel_consumption(data, cost_fn=lambda x: x)



def part2(data: List[int]) -> int:
    """
    How much fuel must they spend to align to that position?
    """
    return best_fuel_consumption(data, cost_fn=lambda d: (d *(d+1)//2))
