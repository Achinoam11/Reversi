from rules import Rules
from disk import Disk
import copy
import math
class UtilitySimplePlayer:
    """Class the calculate the utility of every move for the simple player"""
    rules = Rules()

    def choose_move(self, board, possible_moves, color):
        moves_utility = [self.utility(board, move, color) for move in possible_moves]
        return possible_moves[moves_utility.index(max(moves_utility))]

    def utility(self, board, move, color):
        new_board = copy.deepcopy(board)
        self.rules.add_disk(new_board, move, self.rules.create_disk(color))
        possible_moves_for_opponent = self.rules.get_possible_moves(new_board, self.rules.opposite_color(color))
        if not possible_moves_for_opponent:
            return math.inf
        else:
            return self.basic_utility(new_board, color)

    def basic_utility(self, board, color):
        return self.rules.sum_color(board, color) - self.rules.sum_color(board, self.rules.opposite_color(color))







