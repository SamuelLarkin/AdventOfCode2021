import networkx as nx

from collections import Counter 
from typing import (
        Set,
        Tuple,
        )



def load(filename: str = "input.txt") -> nx.Graph:
    G = nx.Graph()
    with open(filename, mode='r', encoding="UTF-8") as cin:
        cin = map(str.strip, cin)
        for line in cin:
            from_, to_ = line.split('-')

            if from_ not in G:
                G.add_node(from_)
            if to_ not in G:
                G.add_node(to_)

            G.add_edge(from_, to_)


    return G



def all_paths(
        graph: nx.Graph,
        allowed_fn,
        path = ('start',),
        ):
    """
    """
    start = path[-1]
    if start == 'end':
        yield path
    else:
        for n in nx.neighbors(graph, start):
            if not allowed_fn(n, path):
                continue
            else:
                yield from all_paths(graph, allowed_fn, path + (n,))




def part1(data: nx.Graph) -> int:
    """
    How many paths through this cave system are there that visit small caves at most once?
    """
    def allowed_fn(n, path) -> bool:
        return not (n.lower() == n and n in path)

    if False:
        for p in all_paths(data, allowed_fn):
            print(p)

    return len(list(all_paths(data, allowed_fn)))




def part2(data: nx.Graph) -> int:
    """
    """
    def allowed_fn(n, path: Tuple) -> bool:
        if n == 'start':
            # Once you leave the start cave, you may not return to it.
            return False

        #print(n, path)
        if n.lower() == n and n in path:
            suspects = filter(lambda p: p.lower() == p, path)
            #suspects = filter(lambda p: not p in ('start', 'end',), suspects)
            suspects = tuple(suspects)
            #print(suspects)
            counts = Counter(suspects + (n,))
            #print(counts)
            counts_of_counts = Counter(counts.values())
            #print(counts_of_counts)
            if 3 in counts_of_counts:
                # We are not allowed to visit a single path more that n twice.
                # A single small cave can be visited at most twice.
                return False
            # Is there more than one path that we are about to visit twice?
            return counts_of_counts.get(2, 1) == 1

        return True

    if False:
        for p in all_paths(data, allowed_fn):
            print(p)

    return len(list(all_paths(data, allowed_fn)))
