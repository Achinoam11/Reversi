from abstract_player import AbstractPlayer
from utility_simple_player import UtilitySimplePlayer

class SimplePlayer(AbstractPlayer):
    """Class that defines a simple player who goes over all the possible moves and evaluates the board
     after making each move. The utility that it assigns to each game board is computed as the number of
    pieces it has on the board minus the number of pieces that its opponent has. If the player has a
    winning state on the board, then the board’s utility is infinity, while if it has a losing state, then
    the utility is -infinity. """

    def __init__(self, color):
        super().__init__(color)
        self.utility = UtilitySimplePlayer()

    def get_move(self, board, possible_moves):
        print(f"Simple player possible moves are: {possible_moves}")
        move = self.utility.choose_move(board, possible_moves, self.color)
        return move