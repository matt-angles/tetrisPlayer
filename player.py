from board import Direction, Rotation, Action

from myplayer import QuadSensei

class Player():
    def choose_action(self, board):
        return NotImplementedError

class YourPlayerName(Player):
    def choose_action(self, board):
        # Try it yourself !
        return NotImplementedError
    
    
# Select your player here
SelectedPlayer = QuadSensei
