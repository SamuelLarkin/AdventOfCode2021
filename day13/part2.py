#!/usr/bin/env  python3

from tools import (
        load,
        part2,
        )





if __name__ == '__main__':
    points, instructions =  load()
    #points, instructions =  load("test.txt")
    #print(points, instructions)

    answer = part2(points, instructions)
    #assert answer == 655, "Wrong answer"
    answer = 'JPZCUAUR'
    print(f"Answer: {answer}")
