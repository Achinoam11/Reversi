from abstract_player import AbstractPlayer
from rules import Rules
import math
import copy
from datetime import datetime
from datetime import timedelta


class StrategyPlayer(AbstractPlayer):
    """Class that defines a player that uses MinMax algorithm to choose his next move. """
    rules = Rules()

    # features = {"number_of_disks": 10/64, "number_of_corners": 100/4, "disks_on_edge": 100/26}

    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        #print(f"Player10 possible moves are: {possible_moves}")
        values = []
        start_time = datetime.now()
        for move in possible_moves:
            new_board = copy.deepcopy(board)
            self.rules.add_disk(new_board, move, self.rules.create_disk(self.color))
            #print(f"from get_move of player10, the move we look at is {move}, it's h is: "
             #     f"{self.minmax(new_board, self.color, start_time)}")
            values.append(self.minmax(new_board, self.color, start_time))
        best_move = possible_moves[values.index(max(values))]
        #print(f"player10 plays {best_move}")
        return best_move

    def minmax(self, board, color, start_time, depth=0):
        """The function will choose the maximum heuristic_evaluation for the DARK player,
         and the minimum for the LIGHT player"""

        if datetime.now() - start_time >= timedelta(seconds=self.time_per_turn):
            print ("time is over")
            return 0

        if depth == 0 or self.rules.end_of_game(board):
            return self.heuristic_evaluation(board, color)

        #if self.rules.end_of_game(board):
            # check if the game is over
            #return self.heuristic_evaluation(board)

        possible_moves = self.rules.get_all_possible_moves(board, self.rules.opposite_color(color))

        if color == self.color:
            value = math.inf
            if not possible_moves:
                value = min(value, self.minmax(board, self.rules.opposite_color(color), \
                                               start_time, depth - 1))
            else:
                for move in possible_moves:
                    new_board = copy.deepcopy(board)
                    # print(f"from minmax, the opposite color turn, the move we look at now is: {move}")
                    self.rules.add_disk(new_board, move, self.rules.create_disk(self.rules.opposite_color(color)))
                    value = min(value, self.minmax(new_board, self.rules.opposite_color(color), \
                                                   start_time, depth - 1))

        else:
            # print (f"the depth is {depth} and the color is {color}")
            value = -math.inf
            if not possible_moves:
                value = max(value, self.minmax(board, self.rules.opposite_color(color), start_time, depth - 1))
            else:
                for move in possible_moves:
                    new_board = copy.deepcopy(board)
                    self.rules.add_disk(new_board, move, self.rules.create_disk(self.rules.opposite_color(color)))
                    value = max(value, self.minmax(new_board, self.rules.opposite_color(color), start_time, depth - 1))

        # print (f"from minmax, the value to be return from depth {depth} is {value}")
        return value

    def heuristic_evaluation(self, board, color):
        if self.rules.end_of_game(board):
            # in case this is the end of the game
            winner = self.rules.find_winner(board)
            if winner == self.color:
                return math.inf
            elif winner == self.rules.opposite_color(self.color):
                return -math.inf
            else:
                return 0
        h = 0
        opposite_possible_moves = self.rules.get_all_possible_moves(board, self.rules.opposite_color(color))
        if self.rules.get_num_of_corners(board, self.color) > \
                self.rules.get_num_of_corners(board, self.rules.opposite_color(self.color)):
            h += 100000
        elif self.rules.get_num_of_corners(board, self.color) < \
                self.rules.get_num_of_corners(board, self.rules.opposite_color(self.color)):
            h -= 100000
            # number of corners

        opponent_possible_moves_on_the_edge = 0

        for move in opposite_possible_moves:
            if move[0] == 0 or move[0] == board.size - 1 or move[1] == 0 or move[1] == board.size - 1:
                opponent_possible_moves_on_the_edge = 1

        if color == self.color:
            h -= 2000 * opponent_possible_moves_on_the_edge
            h -= 200000 * self.opposite_corners(board, opposite_possible_moves)
            # possibility for opponent to get corners
        else:
            h += 2000 * opponent_possible_moves_on_the_edge
            h += 200000 * self.opposite_corners(board, opposite_possible_moves)
            # possibility for opponent to get corners

        # h -= 5000 * len(self.rules.get_edge_possible_moves(board, self.rules.opposite_color(self.color)))
        # the number of opponent possible moves on edge next to our disks on edge
        # Sadly not working well

        h += 4000 * self.rules.on_the_edge_without_neighbors(board, self.color)
        # number of our disks on edge without neighbors

        h -= 4000 * self.rules.on_the_edge_without_neighbors(board, self.rules.opposite_color(self.color))
        # number of opponent disks on the edge without neighbors

        h += self.rules.sum_color(board, self.color) - self.rules.sum_color(board, \
                                                                            self.rules.opposite_color(self.color))
        # difference in the number of disks on the board

        h -= 10 * self.rules.get_number_of_disks_on_square(board, 1, board.size - 2, self.color)
        # number of disks in the lines\rows that close to the edges

        h += 10 * self.rules.get_number_of_disks_on_square(board, 1, board.size - 2, \
                                                           self.rules.opposite_color(self.color))
        # number of opponent disks in the lines\rows that close to the edges

        h += 20 * self.rules.get_number_of_disks_on_square(board, 0, board.size - 1, self.color)
        # number of disks on edge

        h -= 20 * self.rules.get_number_of_disks_on_square(board, 0, board.size - 1, \
                                                           self.rules.opposite_color(self.color))
        # number of opponent disks on edge
        
        return h

    def opposite_corners(self, board, opposite_possible_moves):
        count = 0
        if (0, 0) in opposite_possible_moves:
            count += 1
        if (0, board.size - 1) in opposite_possible_moves:
            count += 1
        if (board.size - 1, 0) in opposite_possible_moves:
            count += 1
        if (board.size - 1, board.size - 1) in opposite_possible_moves:
            count += 1
        return count