# Tetris Player
An algorithm that plays Tetris and tries to get as many points as possible. 

## Description
### The Game
On a board of default size 24x10, blocks of four squares known as _Tetronimos_ drop. The player must guide them to a good landing place to score points.
When one or more lines is completed all the blocks in those lines are eliminated, the blocks above drop, and you score extra points.
The goal is to score as many points as possible before the blocks reach the top of the screen.

This version also has additional features:
- The next block that is going to drop is known
- The more lines you complete at once, the more points you get, exponentially in this order: 25, 100, 400, 1600
- There is no time constraint, but there is a defined amount of blocks to land (default: 400)
- You can discard a tetronimo you don't like up to 10 times per game
- You can substitute a tetronimo for a bomb to destroy all the immediately surrounding blocks

### The Autoplayer
My autoplayer tries every move possible with the current and next block. It then attributes a custom value to each move,
depending on how good it think it is, and plays the move with the lowest value.

Here is how the value is calculated:
- \+ Average height on the board
- \+ 3 * Bumpiness: is the board regular or not
- \+ 25 * Number of holes in the board
- If the move completes one line, add to the value if the height of the board is high else substract
- If the move completes more than one line, substract to the value exponentially

Hence my strategy is to attempt to create an rectangular shape on the board, but to penalize completing single lines if its not necessary.
Thus the heuristic of holes and lines completed is overweighted.

## Attempting it yourself
Using grader.py, this autoplayer gets an average score of 24,571.875. However, the theoretical maximum would be around 60k.
So there is **plenty** of space for a much better AI, and I encourage you to use this repo to try to improve my score!

### How to code
The algorithm's code must be written in player.py. It should be inside a class derived from Player, and in order to run be the SelectedPlayer. 
The method `choose_action` will be called by the game to get the next action(s) to do. `choose_action` should return an action or a list of actions (from the enums `Action`, `Direction` and `Rotation`). It can also yield actions and work as a generator if that's more convenient.

The actual core tetris code is in board.py if you want to take a look.
Here's a list of features you might find very useful for your AI:
- The `Shape` enum
- The board (your parameter), using the methods `move`, `rotate`, `bomb`, `discard`, `skip` and `clone`
- Board also has the attributes: `falling` for the current shape, `next` for the next shape and `cells` for the current cells on the board.
- Some constants of the game can be tweaked for testing in constants.py - most importantly the `DEFAULT_SEED` to try out different situations

Then, the game can be launched with cmdline.py (ncurses), visual.py (tkinter) or visual-pygame.py (pygame).
The pygame version runs the best, so I would recommend that.

In each of these version you can also play in manual mode with -m, but I would recommend playing online with websites such as tetr.io if you really want
to get a feel for the game.

Finally you can run grader.py to try the player against multiple seed and compute an average score.

Good luck!

## Credit
The Tetris game was written by Tobias Kappé and Mark Handley in the context of the engf0034 module at UCL. I wrote the AI and grader.
