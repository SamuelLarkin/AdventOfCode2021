import pytest

from ..tools import (
        Player,
        Player2,
        move,
        part2,
        play,
        )



@pytest.mark.parametrize(
        "player,move,position,score",
        (
            ( Player(4, 0), 1+2+3, 10, 10 ),
            ( Player(8, 0), 4+5+6, 3, 3 ),
            ( Player(10, 10), 7+8+9, 4, 14 ),
            ( Player(3, 3), 10+11+12, 6, 9 ),
            ( Player(4, 14), 13+14+15, 6, 20 ),
            ( Player(6, 9), 16+17+18, 7, 16 ),
            ( Player(6, 20), 19+20+21, 6, 26 ),
            ( Player(7, 16), 22+23+24, 6, 22 ),
            )
        )
def test_player(player: Player, move: int, position: int, score: int):
    player.move(move)
    assert player.position == position
    assert player.score == score



@pytest.mark.parametrize(
        "player,step,position,score",
        (
            ( Player2(4, 0), 1+2+3, 10, 10 ),
            ( Player2(8, 0), 4+5+6, 3, 3 ),
            ( Player2(10, 10), 7+8+9, 4, 14 ),
            ( Player2(3, 3), 10+11+12, 6, 9 ),
            ( Player2(4, 14), 13+14+15, 6, 20 ),
            ( Player2(6, 9), 16+17+18, 7, 16 ),
            ( Player2(6, 20), 19+20+21, 6, 26 ),
            ( Player2(7, 16), 22+23+24, 6, 22 ),
            )
        )
def test_move(player: Player2, step: int, position: int, score: int):
    p = move(player, step)
    assert p.position == position
    assert p.score == score



def test_play():
    answer = play(Player(4), Player(8))
    assert answer == 739_785



def test_part2():
    answer = part2(Player(4), Player(8), 21)
    assert answer == 444356092776315
