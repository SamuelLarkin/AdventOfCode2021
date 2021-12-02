from typing import List



def load(input_data_fn: str = 'input.txt') -> List[int]:
    with open('input.txt', mode='r', encoding='UTF-8') as data:
        data = map(int, data.readlines())
        data = list(data)

    return data



def triplet_sum(data: List[int]) -> List[int]:
    data = zip(data, data[1:], data[2:])
    data = map(lambda a: sum(a), data)
    data = list(data)

    return data



def consecutive_diff(data: List[int]) -> List[int]:
    data = zip(data, data[1:])
    data = map(lambda a: a[1] - a[0], data)
    data = filter(lambda a: a > 0, data)
    data = list(data)

    return data
