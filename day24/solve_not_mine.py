#!/usr/bin/env  python3

# https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpu84cj/?utm_source=share&utm_medium=web2x&context=3
# https://topaz.github.io/paste/#XQAAAQBpBQAAAAAAAAA0m0pnuFI8c/fBNAn6x25rti77on4e8DYCelyI4Xj/SWO86l3MhYKSt/IwY1X8XDsPi6oUd359E/fP3WUCy+Hd0NBX3ScDH1UMDMoIn89DqtRJAkuU26H+bJQMhuQJZGvHfbRq+cNenkcVuZMyoJg2X38kr/tdzPWRs0R3nEQAYf3r0cXmSlac2aJH0P2sl7z4weDgKeKkKfE5swiQJ2MN12HwuoRR3LBTiJQjtT73JpWF+KtQBulka0/rhUSDOrztKM4biu1JoxqydIgyDfWupEKKtAiW75B1XW73P7TSQe8BI9O2T12ql8E/CBnsomkNwZLvIqQuyxA8lRBFyEb7T2Ofx8p8uaMPHbMv786Ho5P2KtCBwYdoX3z3fIV+cETYydTzjakKrUdUMq7dRV/kbM91elWwnwaxWByBhJS7jtOshbq8mO2W3BfCQ48WxEmwVrceIMSV2txALQlDxsy1lduebYKTzWCNl58cRdbnvICOxfoV9eofWAd6dE/BpGhxqy4snlEFMPa26JyVjXfXpD+Sh4Vchgcj3Kov+/Dy78f33t8khcwkJaKtJgg7+E+i+YRS7ql81NzjItIrTm1KnqMrxqq0Hl+1zxqTbrn9BDkVsNNu9Mbab72K6iYsNta7J52Io0LObTiUJ289oAzc4RGO/ZCtY4a9Pv0VI4kTpEYmTEUYac9twmKZkClSuD/U8SNOLFtHUI9giLRa+6nUHUGr7LCCvmI3lP10Nh0MlDB3Olffd11IPud3A9Wh9M6eEaXcq0bzn7BUOrQ8ff+FFf33ixp2

import sys

from collections import (
        defaultdict,
        )
from typing import (
        Dict,
        List,
        Sequence,
        Tuple,
        )



Solution = List[Tuple[int, int]]
Solutions = Dict[int, Solution]



class Solver:
    """
    """
    NUM_DIGITS: int= 14
    NUM_SUB_INSTRUCTIONS: int = 18


    def __init__(self, instructions: List[str]):
        self.consts: Sequence[Tuple[int, int, int]] = [
                (
                    int(l[self.NUM_SUB_INSTRUCTIONS*i+4][2]),
                    int(l[self.NUM_SUB_INSTRUCTIONS*i+5][2]),
                    int(l[self.NUM_SUB_INSTRUCTIONS*i+15][2]),
                    )
                for i in range(self.NUM_DIGITS)
                ]

        self.levels: List[Solutions] = [None] * self.NUM_DIGITS
        self._build_deps([0])


    def _find_solutions(
            self,
            A: int,
            B: int,
            C: int,
            zl: List,
            ):
        """
        """
        sols = defaultdict(list)
        for w in range(9, 0, -1):
            for z in zl:
                for a in range(A):
                    pz = z * A + a
                    if pz % 26 + B == w:
                        if pz // A == z:
                            sols[pz].append((w, z))

                    pz =(z - w - C) // 26 * A + a
                    if pz % 26 + B != w:
                        if pz // A * 26 + w + C == z:
                            sols[pz].append((w, z))

        return sols


    def _build_deps(
            self,
            zl: List[int],
            ) -> None:
        """
        """
        constants = enumerate(self.consts)
        constants = list(constants)
        for i, (A, B, C) in reversed(constants):
            sols = self._find_solutions(A, B, C, zl)

            assert sols
            self.levels[i] = sols

            zl = list(sols.keys())


    @property
    def biggest(self) -> str:
        """
        What is the largest model number accepted by MONAD?
        """
        return self.solve(0, largest=True)



    @property
    def smallest(self) -> str:
        """
        What is the smallest model number accepted by MONAD?
        """
        return self.solve(0, largest=False)



    def solve(
            self,
            z: int,
            largest : bool=False,
            ) -> bool:
        def helper(
                i: int,
                z: int,
                sol: List,
                largest : bool=False,
                ):
            if i == 14:
                return ''.join(str(j) for j in sol)

            if z not in self.levels[i]:
                return None

            for w, nz in sorted(self.levels[i][z], reverse=largest):
                ts = (*sol, w)
                answer = helper(i+1, nz, list(ts), largest)
                if answer is not None:
                    return answer

        return helper(0, z, [], largest)





if __name__ == '__main__':
    assert len(sys.argv) > 1, "You must provide an input file"
    with open(sys.argv[1], mode='r', encoding='UTF-8') as cin:
        cin = map(str.strip, cin)
        l = list(map(str.split, cin))

    solver = Solver(l)

    p1 = solver.biggest
    assert p1 == '94992994195998'
    print(p1)

    p2 = solver.smallest
    print(p2)
    assert p2 == '21191861151161'
