from board import Direction, Rotation
from constants import BOARD_WIDTH, BOARD_HEIGHT

startWidth = (BOARD_WIDTH//2) - BOARD_WIDTH
endWidth = BOARD_WIDTH - (BOARD_WIDTH//2) -1

class Player():
    def choose_action(self, board):
        return NotImplementedError

class QuadSensei(Player):
    def applyMove(self, board, pos, rot):
        move = []
        try:
            for _ in range(rot):
                board.rotate(Rotation.Clockwise)
                move.append(Rotation.Clockwise)
            if pos > 0:
                for _ in range(pos):
                    board.move(Direction.Right)
                    move.append(Direction.Right)
            if pos < 0:
                for _ in range(-pos):
                    board.move(Direction.Left)
                    move.append(Direction.Left)
            board.move(Direction.Drop)
            move.append(Direction.Drop)
            return board, move
        except:
            # Signal invalid move
            return None, None
        
    def height(self, board):
        heights = []
        for x in range (BOARD_WIDTH):
            for y in range (BOARD_HEIGHT):
                if (x,y) in board.cells:
                    heights.append(BOARD_HEIGHT - y)
                    break;
                elif y == BOARD_HEIGHT-1:
                    heights.append(0)
        return heights
        
    def average_height(self, heights):
        return sum(heights)
    
    def bumpiness(self, heights):
        return sum(abs(heights[i] - heights[i+1]) for i in range(BOARD_WIDTH-1))
    
    def holes(self, board):
        nHoles = 0
        for x in range(BOARD_WIDTH):
            emptySpace = None
            for y in range(BOARD_HEIGHT-1, -1, -1):
                if (x, y) not in board.cells:
                    emptySpace = y
                if (x,y) in board.cells and emptySpace is not None:
                    nHoles += emptySpace - y
                    emptySpace = None
        return nHoles

    def lines(self, board, currentScore):
        scored = board.score - currentScore
        # Wrong values but it works...
        if 50 < scored < 400:
            return 1
        elif 400 < scored < 800:
            return 2
        elif 800 < scored < 1600:
            return 3
        elif 1600 < scored:
            return 4
        else:
            return 0
    
    def score(self, board, currentScore):
        score = 0
        heights = self.height(board)
        score += self.average_height(heights)
        score += self.bumpiness(heights) * 3
        score += self.holes(board) * 25
        
        lines = self.lines(board, currentScore)
        if lines != 1:
            score -= 25 ** lines
        else:
            score += 4 * (12 - max(heights))
        return score
    
    def best_move(self, board):
        bestMove = [Direction.Drop]
        currentScore = board.score  # used for scoring later
        
        bestScore = 0
        baselineBoard = board.clone() ; baselineBoard.move(Direction.Drop)
        bestScore = self.score(baselineBoard, currentScore)    # Baseline score. Not playing isn't an option
        

        # Simulating all possibles moves with current and next block
        for rot1 in range(4):
            for pos1 in range(startWidth, endWidth):
                for rot2 in range(4):
                    for pos2 in range(startWidth, endWidth):
                        fstBoard, fstMove = self.applyMove(board.clone(), pos1, rot1)
                        if fstBoard is None:    # Move is not valid
                            continue
                        workBoard, sndMove = self.applyMove(fstBoard.clone(), pos2, rot2)
                        if workBoard is None:
                            continue
                        else:
                            move = fstMove + sndMove
                            score = self.score(workBoard, currentScore)
                            if score <= bestScore:
                                bestScore = score
                                bestMove = move

        return bestMove
    
    def choose_action(self, board):
        bestMove = self.best_move(board)
        return bestMove
