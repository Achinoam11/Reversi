if color == "DARK":
else:
for i, pair in enumerate(pairs):
    delta = self.create_delta(pair, color)
    j = 1
    while True:
        next_disk = (pair[0][0] + j * delta[0], pair[0][1] + j * delta[1])
        if not board.in_board(next_disk):
            break
        if board.if_space_empty(next_disk):
            if next_disk not in possible_moves:
                possible_moves.append(next_disk)
            count_turns.append(j)
            # board = self.add_disk(board, next_disk, pair[1], Disk.LIGHT)
            break
        j += 1

# next_disk = self.create_next_disk(pair, j, delta, color)
# if not board.in_board(next_disk):
#   break


delta = self.create_delta((place, neighbor)) ###
                j = 1
                while True:
                    next_disk = self.create_next_disk((place, neighbor), j, delta)
                    if not board.in_board(next_disk):
                        break
                    if board.if_space_empty(next_disk):
                        if next_disk not in possible_moves:
                            possible_moves.append(next_disk)
                        count_turns.append(j)
                        # board = self.add_disk(board, next_disk, pair[0], Disk.DARK)
                        break
                    j += 1

# game_is_on = True
# while game_is_on:
game_is_on = game.the_game(0)

# g1 = Game(8)
b1 = Board(8)
print(b1)
r1 = Rules()
r1.add_disk(b1, (2, 4), Disk.DARK)
print(b1)
r1.add_disk(b1, (2, 5), Disk.LIGHT)
print(b1)
r1.add_disk(b1, (5, 3), Disk.DARK)
print(b1)
# print(r1.get_possible_moves(b1, "LIGHT"))
# print(r1.should_turn_disks(b1, (1,4), "DARK"))
print(b1)
print(r1.get_possible_moves(b1, "DARK"))
p1 = RealPlayer("DARK", 9)
p1.get_move(b1, r1.get_possible_moves(b1, p1.color))
print(b1)


def copy_board(self):
    new_board = copy.deepcopy()
    ard(self.size)
    for i, row in enumerate(self.board):
        for j, col in enumerate(row):
            new_board[i][j] = self.board[i][j]
    new_board
    return Board()

    def the_game(self, num):
        possible_moves = self.rules.get_possible_moves(self.board, self.players[num].color)
        if self.rules.if_board_full(self.board):
            #check if the board is full
            self.rules.find_winner(self.board)

        elif not possible_moves:
            #if player don't have any possible moves to play
            if not self.rules.get_possible_moves(self.board, self.rules.opposite_color(self.players[num].color)):
                #if both player don't have moves, end the game and declare winner
                self.rules.find_winner(self.board)
            else:
                #if other player have moves, let him play
                self.the_game(self.get_other_player(num))
        else:
            #if the player have moves to do, let him play
            current_move = self.players[num].get_move(self.board, possible_moves)
            print (f"The {self.players[num].color} player plays: {current_move}")
            self.rules.add_disk(self.board, current_move, self.rules.create_disk(self.players[num].color))
            print(self.board)
            self.the_game(self.get_other_player(num))

            self.features["number_of_disks"] * (dark["number_of_disks"] - light["number_of_corners"]) + self.features["number_of_corners"]\
                                                * (dark["number_of_corners"] - light["number_of_corners"])