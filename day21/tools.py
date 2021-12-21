#!/usr/bin/env  python3

from collections import namedtuple
from dataclasses import dataclass
from functools import lru_cache
from itertools import (
        count,
        product,
        )
from typing import (
        Generator,
        Tuple,
        )


@dataclass
class Player:
    """
    """
    position: int
    score: int = 0

    def __post__init__(self):
        assert 0 < self.position <= 10


    def move(self, steps: int):
        steps += self.position
        while steps > 10:
            steps -= 10
        self.position = steps
        self.score += self.position



def roll_deterministicr_dice() -> int:
    """
    """
    while True:
        for value in range(1, 101):
            yield value



def play(player1: Player, player2: Player, winning_score: int = 1000) -> int:
    """
    What do you get if you multiply the score of the losing player by the
    number of times the die was rolled during the game?
    """
    players = [ player1, player2 ]
    die = roll_deterministicr_dice()
    for step in count():
        player_id = step % 2
        player = players[player_id]
        move = sum((next(die), next(die), next(die)))
        player.move(move)
        #print(player_id, player.score)
        if player.score >= winning_score:
            break

    loser = (step + 1) % 2

    return 3 * (step + 1) * players[loser].score



Player2 = namedtuple('Player2', ('position', 'score'))



def move(player: Player2, steps : int) -> Player2:
    """
    """
    position = steps + player.position
    while position > 10:
        position -= 10

    return Player2(position, player.score + position)



def diracr_dice() -> Generator[int, None, None]:
    """
    """
    yield from product(range(1, 4), repeat=3)



@lru_cache(None)
def part2_helper(
        player_current: Player2,
        player_next: Player2,
        winning_score : int = 21,
        ) -> Tuple[int, int]:
    """
    """
    if player_next.score >= winning_score:
        return 1, 0

    games = [
            part2_helper(player_next, move(player_current, sum(die_values)), winning_score)
            for die_values in diracr_dice()
            ]

    return (
            sum(g[1] for g in games),
            sum(g[0] for g in games),
            )



def part2(player1: Player, player2: Player, winning_score: int = 21) -> int:
    """
    Find the player that wins in more universes; in how many universes does
    that player win?
    """
    player1 = Player2(player1.position, player1.score)
    player2 = Player2(player2.position, player2.score)
    p1_wins, p2_wins = part2_helper(player1, player2, winning_score)

    return max(p1_wins, p2_wins)






if __name__ == '__main__':
    answer = play(Player(4), Player(8))
    p = Player2(4, 0)
    answer = part2(Player(4), Player(8))
    print(answer)
