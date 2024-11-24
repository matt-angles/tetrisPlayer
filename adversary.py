from board import Shape
from exceptions import BlockLimitException
from random import Random


class Adversary:
    def choose_block(self, board):
        raise NotImplementedError


class RandomAdversary(Adversary):
    random = None
    blocks = None

    def __init__(self, seed, blocks=None):
        self.random = Random(seed)
        self.blocks = blocks

    def choose_block(self, board):
        if self.blocks is not None:
            if self.blocks == 0:
                raise BlockLimitException()
            else:
                self.blocks -= 1
        return self.random.choice(list(Shape)[:-1])
