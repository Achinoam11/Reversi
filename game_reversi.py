from board import Board
from disk import Disk
from rules import Rules
from real_player import RealPlayer
from random_player import RandomPlayer
from simple_player import SimplePlayer
from player10 import Player10

class Game:

    def __init__(self):
        self.players = [Player10("LIGHT"), RandomPlayer("DARK")]
        self.board = Board(8)#.start_board()
        self.rules = Rules()

    def display_board(self):
        print(self.board)

    def get_other_player(self, num):
        if num == 0:
            return 1
        elif num == 1:
            return 0

    def the_game(self, num):
        possible_moves = self.rules.get_possible_moves(self.board, self.players[num].color)
        if self.rules.end_of_game(self.board):
            #check if the game is over
            winner = self.rules.find_winner(self.board)
            if not winner:
                print("Game over! It's a tie!")
            else:
                print(f"Game over! The winner is the {winner} player!!!")

        elif not possible_moves:
                #if other player have moves, let him play
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
