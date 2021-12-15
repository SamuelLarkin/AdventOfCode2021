import heapq
import networkx as nx

from board import Board
from itertools import chain
from queue import PriorityQueue
from typing import (
        List,
        )



def load(filename: str = "input.txt") -> Board:
    with open(filename, mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        data = [ list(map(int, l)) for l in cin ]
        y = len(data)
        x = len(data[0])
        board = Board((x,y))
        board.populate(chain.from_iterable(zip(*data)))

    return board



def convert2graph(board: Board):
    G = nx.DiGraph()
    for coord, score in board.iterdata():
        for n in board.neighbours(coord, include_diagonals=False):
            G.add_edge(coord, n, weight=board[n]) 

    return G



def part1(board: Board) -> int:
    """
    What is the lowest total risk of any path from the top left to the bottom right?
    """
    G = convert2graph(board)
    start = (0, 0)
    end = board.dimensions
    end = (end[0]._size-1, end[1]._size-1)

    path = nx.shortest_path(G, start, end, 'weight')

    # Recall that the starting position's score is not tallied.
    return sum(board[c] for c in path) - board[start]



def part2(board: Board) -> int:
    """
    What is the lowest total risk of any path from the top left to the bottom right?
    """
    start = (0, 0)
    end = board.dimensions
    end = (end[0]._size-1, end[1]._size-1)

    # Extend the board
    b2 = Board(((end[0]+1)*5, (end[1]+1)*5))
    for i in range(5):
        io = i * (end[0]+1)
        for j in range(5):
            jo = j * (end[1]+1)
            for k in range(end[0]+1):
                for l in range(end[1]+1):
                    value = board[(k,l)] + (i+j)
                    if value > 9:
                        # This would probably not work if we had extended the grid more than 5 times
                        value = value % 10 + 1
                    b2[(io+k, jo+l)] = value

    #b2.draw(use_borders=False)
    G = convert2graph(b2)

    end = b2.dimensions
    end = (end[0]._size-1, end[1]._size-1)
    path = nx.shortest_path(G, start, end, 'weight')

    # Recall that the starting position's score is not tallied.
    return sum(b2[c] for c in path) - board[start]



def part1_too_slow(board: Board) -> int:
    """
    What is the lowest total risk of any path from the top left to the bottom right?
    """
    assert False, "TOOOOO SLOW"
    end = board.dimensions
    end = (end[0]._size-1, end[1]._size-1)
    q = [(0, ((0,0),))]
    while len(q) > 0:
        (score, path) = heapq.heappop(q)
        current_position = path[-1]
        if current_position == end:
            for p in path:
                board[p] = "X"
            board.draw(use_borders=False)
            return score

        for n in board.neighbours(current_position, include_diagonals=False):
            if n not in path:
                heapq.heappush(q, (score+board[n], path + (n,)))

    return None
