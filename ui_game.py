from game_reversi import Game
#from rules import Rules

class ReversiUI:

    @staticmethod
    def run_game():
        game = Game()
        game.display_board()
        print ("The DARK player starts")
        game.the_game(1)

if __name__ == "__main__":
    ReversiUI.run_game()


