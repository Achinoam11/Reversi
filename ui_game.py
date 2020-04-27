from game_reversi import Game
#from rules import Rules

class ReversiUI:

    @staticmethod
    def run_game():
        game = Game()
        game.display_board()
        print("The DARK player starts")
        game.the_game(1)
        w = game.winner
        return w


if __name__ == "__main__":
    number_of_games = 1
    statistics = {"DARK": 0, "LIGHT": 0, "Tie": 0}

    for i in range(number_of_games):
        winner = ReversiUI.run_game()
        statistics[winner] += 1
    print(statistics)


