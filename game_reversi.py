from board import Board
from disk import Disk
from rules import Rules
from real_player import RealPlayer
from random_player import RandomPlayer
from simple_player import SimplePlayer
from player10 import Player10
from strategy_player import StrategyPlayer

class Game:
    """Class that run the game, and hold all the game parameters"""

    def __init__(self):
        self.players = [Player10("LIGHT"), RealPlayer("DARK")]
        self.board = Board(8)#.start_board()
        self.rules = Rules()
        self.winner = None
    
    def display_board(self):
        print(self.board)

    def get_other_player(self, num):
        if num == 0:
            return 1
        elif num == 1:
            return 0

    def the_game(self, num):
        possible_moves = self.rules.get_all_possible_moves(self.board, self.players[num].color)
        print(f"from the_game, the possible moves are: {possible_moves}")
        if self.rules.end_of_game(self.board):
            #check if the game is over
            winner = self.rules.find_winner(self.board)
            if winner == "Tie":
                print("Game over! It's a tie!")
            else:
                print(f"Game over! The winner is the {winner} player!!!")
            self.winner = winner

        elif not possible_moves:
                #if the other player has moves, let them play
                self.the_game(self.get_other_player(num))

        else:
            #if the player have moves to do, let him play
            while True:
                current_move = self.players[num].get_move(self.board, possible_moves)
                print(f"The {self.players[num].color} player plays: {current_move}")
                try:
                    self.rules.add_disk(self.board, current_move, self.rules.create_disk(self.players[num].color))
                    break
                except ValueError:
                    print("The move you played is illegal. Try again")
            print(self.board)
            self.the_game(self.get_other_player(num))




if __name__ == "__main__":
    d1 = Disk.NONE
    d2 = Disk.LIGHT
    print(d1.value + d2.value + 5)
