from board import Board
from player import SelectedPlayer
from adversary import RandomAdversary
from exceptions import BlockLimitException

from time import time
from random import randint

INTERVAL = 5    # interval to display score in seconds

def test_seed(seed):
    board = Board(10, 24)
    player = SelectedPlayer()
    adversary = RandomAdversary(seed, 400)
    
    try:
        timer = time()
        for move in board.run(player, adversary):
            if time() - timer > INTERVAL:
                timer = time()
                print(board.score)
        return board.score, False
    except BlockLimitException:
        return board.score, True


seeds = [42, 1, 666, 110] + [randint(0, 999) for _ in range(4)]
finalScore = 0
for i, seed in enumerate(seeds):
    print(f"Grading Seed #{i+1}: {seed}")
    print("####")
    seedScore, allBlocks = test_seed(seed)
    finalScore += seedScore
    if allBlocks:
        print(f"Used all blocks! Score: {seedScore}")
    else:
        print(f"Died. Score: {seedScore}")
    print("####\n")

finalScore /= len(seeds)
print(f"Your final score is: {finalScore}")