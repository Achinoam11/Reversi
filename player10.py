from abstract_player import AbstractPlayer
from rules import Rules
import math
import copy

class Player10(AbstractPlayer):
    """Class that defines a player that uses MinMax algorithm to choose his next move. """
    rules = Rules()
    features = {"number_of_disks": 8, "number_of_corners": 10, "disks_on_edge": 9}

    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        print(f"Player10 possible moves are: {possible_moves}")
        values = []
        for move in possible_moves:
            new_board = copy.deepcopy(board)
            self.rules.add_disk(new_board, move, self.rules.create_disk(self.color))
            values.append(self.minmax(new_board, self.color))
        best_move = possible_moves[values.index(max(values))]
        print(f"player10 plays {best_move}")
        return best_move

    def minmax(self, board, color, depth=4):
        """The function will choose the maximum heuristic_evaluation for the DARK player,
         and the minimum for the LIGHT player"""

        if depth == 0 or self.rules.end_of_game(board):
            return self.heuristic_evaluation(board)

        if color == self.color:
            value = -math.inf
            for move in self.rules.get_possible_moves(board, color):
                new_board = copy.deepcopy(board)
                print(f"from minmax, the move we look at now is: {move}")
                self.rules.add_disk(new_board, move, self.rules.create_disk(color))
                value = max(value, self.minmax(new_board, self.rules.opposite_color(color), depth - 1))
        else:
            value = math.inf
            for move in self.rules.get_possible_moves(board, color):
                new_board = copy.deepcopy(board)
                self.rules.add_disk(new_board, move, self.rules.create_disk(color))
                value = min(value, self.minmax(new_board, self.rules.opposite_color(color), depth - 1))
        return value

    def heuristic_evaluation(self, board):
        if self.rules.end_of_game(board):
            #in case this is the end of the game
            winner = self.rules.find_winner(board)
            if winner == "DARK":
                return math.inf
            elif winner == "LIGHT":
                return -math.inf
            else:
                return 0

        dark = {"number_of_disks": self.rules.sum_color(board, "DARK"), "number_of_corners": \
            self.rules.get_num_of_corners(board, "DARK"), "disks_on_edge": self.rules.get_on_edge(board, "DARK")}
        light = {"number_of_disks": self.rules.sum_color(board, "LIGHT"), "number_of_corners": \
            self.rules.get_num_of_corners(board, "LIGHT"), "disks_on_edge": self.rules.get_on_edge(board, "DARK")}
        h = sum({self.features[parameter] * (dark[parameter] - light[parameter]) for parameter in self.features.keys()})
        return h



