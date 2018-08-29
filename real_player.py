from abstract_player import AbstractPlayer
from rules import Rules

class RealPlayer(AbstractPlayer):
    """Class defines a real player choosing how to play"""

    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        print(f"Your possible moves are: {possible_moves}")
        str_move = input(f"Please choose your move row,col: ").split(',')
        move = (int(str_move[0]), int(str_move[1]))
        return (move)
        #return r.add_disk(board, move, disk)




