from typing import (
        List,
        )



def aggregate(data: List[int]) -> List[int]:
    counts = [ 0 for _ in range(9) ]
    for d in data:
        counts[d] += 1

    return counts



def load(filename: str = "input.txt") -> List[int]:
    with open(filename, mode="r", encoding="UTF-8") as cin:
        data = cin.readline()
        data = data.strip()
        data = data.split(',')
        data = list(map(int, data))

    return aggregate(data)



def play(data: List[int], days = 80) -> int:
    for d in range(days):
        new_borns = data[0]
        for j in range(8):
            data[j] = data[j+1]

        data[6] += new_borns
        data[8] = new_borns
        #print(d+1, data)

    return sum(data)
