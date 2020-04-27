from disk import Disk
from board import Board

class Rules:
    """Class that defines all the possible moves, and execute moves"""
    """
    def __init__(self, board, color):
        
        self.board = board
        self.color = color
        
        self.moves = set()

    #def find_2_different(self):
"""

    def for_valid_delta(self, num):
        if num >= 1:
            return 1
        elif num <= -1:
            return -1
        elif num == 0:
            return 0
        else:
            raise "Not a valid number"

    def valid_delta(self, delta):
        return self.for_valid_delta(delta[0]), self.for_valid_delta(delta[1])

    def multiply_delta(self, delta, num):
        return delta[0] * num, delta[1] * num

    def sum_2_places(self, place1, place2):
        new_place = (place1[0] + place2[0], place1[1] + place2[1])
        return new_place

    def smaller_place(self, place1, place2):
        p1 = place1[0] + place1[1]
        p2 = place2[0] + place2[1]
        if p1 < p2:
            return place1
        else:
            return place2

    def bigger_place(self, place1, place2):
        p1 = place1[0] + place1[1]
        p2 = place2[0] + place2[1]
        if p1 > p2:
            return place1
        else:
            return place2

    def abs_place(self, place):
        return abs(place[0]), abs(place[1])

    def create_delta(self, pair, color):
        if color == "DARK":
            return self.valid_delta((pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])) #self.for_valid_delta(pair[1][0] - pair[0][0]), self.for_valid_delta(pair[1][1] - pair[0][1])
        elif color == "LIGHT":
            return self.valid_delta((pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])) #self.for_valid_delta(pair[0][0] - pair[1][0]), self.for_valid_delta(pair[0][1] - pair[1][1])
        else:
            print("Invalid color")

    def create_first_disk(self, pair, delta, color):
        if color == "DARK":
            return self.sum_2_places(pair[1], delta)
        else:
            return self.sum_2_places(pair[0], self.multiply_delta(delta, -1))

    def create_next_disk(self, place, delta, color):
        if color == "DARK":
            return self.sum_2_places(place, delta)
        else:
            return self.sum_2_places(place, self.multiply_delta(delta, -1))

    def get_possible_moves(self, board, pairs, color):
        possible_moves = []
        for pair in pairs:
            delta = self.create_delta(pair, "DARK")
            current_place = self.create_first_disk(pair, delta, color)
            while board.in_board(current_place) and board.board[current_place[0]][current_place[1]].name != color:
                if board.if_space_empty(current_place):
                    if current_place not in possible_moves:
                        possible_moves.append(current_place)
                    break
                current_place = self.create_next_disk(current_place, delta, color)
        return possible_moves

    def get_all_possible_moves(self, board, color):
        pairs = board.find_2_different()
        all_possible_moves = self.get_possible_moves(board, pairs, color)
        return all_possible_moves

    def get_edge_possible_moves(self, board, color):
        color_on_edge = self.get_on_edge(board, color)
        pairs = []
        for place_on_edge in color_on_edge:
            pairs.extend(self.get_pairs_on_edge(board, place_on_edge))
        possible_moves_on_edge = self.get_possible_moves(board, pairs, color)
        return possible_moves_on_edge


    def add_disk(self, board, place, disk):
        if place in self.get_all_possible_moves(board, disk.name):
            board.board[place[0]][place[1]] = disk
            self.should_turn_disks(board, place, disk.name)
            return board
        else:
            raise ValueError("from add_disk: Illegel move!")
            #print("from add_disk: Illegel move!")
            #return board
            #new_place = input("The move that you chose is illegal. Please choose another move")
            #self.add_disk(board, new_place, disk)

    def opposite_color(self, color):
        if color == "DARK":
            return "LIGHT"
        elif color == "LIGHT":
            return "DARK"
        else:
            print("The color don't exist")
            return

    def should_turn_disks(self, board, place, color):
        """The function get a place where we want to place a new disk, and the color of the disk we want to place.
        The function send to the function 'turn_disks' all the combinations of the current place and the place
        of the disk with the same color the we need to turn the disks between them"""
        for neighbor in board.get_neighbors(place):
            if neighbor[1].name == self.opposite_color(color):
                delta = self.create_delta((place, neighbor[0]), color)
                if neighbor[1].name == "LIGHT":
                    current_place = self.create_first_disk((place, neighbor[0]), delta, color)
                else:
                    current_place = self.create_first_disk((neighbor[0], place), delta, color)

                while board.in_board(current_place):
                    if board.board[current_place[0]][current_place[1]].name == color:
                        board = self.turn_disks(board, place, current_place)
                        break
                    elif board.if_space_empty(current_place):
                        #board.board[current_place[0]][current_place[1]].name == None:
                        break
                    else:
                        current_place = self.create_next_disk(current_place, delta, color)
        return board

    def turn_disks(self, board, place1, place2):
        """Function get to places in the board and turn all the disks between them"""
        delta = self.create_delta((place1, place2), "DARK") #board.board[place1[0]][place1[1]].name)
        current_place = self.sum_2_places(place1, delta)
        while current_place != place2:
            self.turn_disk(board, current_place)
            current_place = self.sum_2_places(current_place, delta)
        return board

    def turn_disk(self, board, place):
        if board.board[place[0]][place[1]] == Disk.DARK:
            board.board[place[0]][place[1]] = Disk.LIGHT
        elif board.board[place[0]][place[1]] == Disk.LIGHT:
            board.board[place[0]][place[1]] = Disk.DARK
        else:
            raise ValueError(f"The place {place} on the board is empty, so can't turn disk")
            #print(f"The place {place} on the board is empty, so can't turn disk")
        return board

    def sum_color(self, board, color):
        """The function sums all the disks in the specified color"""
        sum_of_color = 0
        for i in range(board.size):
            for j in range(board.size):
                if board.board[i][j].name == color:
                    sum_of_color += 1
        return sum_of_color

    def find_winner(self, board):
        if self.sum_color(board, "DARK") > self.sum_color(board, "LIGHT"):
            return "DARK"
        elif self.sum_color(board, "LIGHT") > self.sum_color(board, "DARK"):
            return "LIGHT"
        else:
            return "Tie"

    def if_board_full(self, board):
        full_board = True
        for i, row in enumerate(board.board):
            for j, col in enumerate(row):
                if board.board[i][j].name == "NONE":
                    full_board = False
        return full_board

    def create_disk(self, color):
        if color == "DARK":
            return Disk.DARK
        else:
            return Disk.LIGHT

    def end_of_game(self, board):
        """function check if it is the end of game"""
        if self.if_board_full(board):
            return True
            #check if the board is full
        if not self.get_all_possible_moves(board, "DARK") and not self.get_all_possible_moves(board, "LIGHT"):
            return True
        return False

    def get_num_of_corners(self, board, color):
        corners = 0
        if board.board[0][0].name == color:
            corners += 1
        if board.board[board.size - 1][0].name == color:
            corners += 1
        if board.board[0][board.size - 1].name == color:
            corners += 1
        if board.board[board.size - 1][board.size - 1].name == color:
            corners += 1
        return corners

    def on_the_edge_without_neighbors(self, board, color):
        """The function returns the number of disks with the color specified that are placed on the edge
         and has no neighbors on the edge"""
        disks_on_the_edge_without_neighbors = 0
        disks_on_the_edge = self.get_on_edge(board, color)
        for disk_on_edge in disks_on_the_edge:
            if not self.get_opposite_neighbors_on_edge(board, disk_on_edge):
                disks_on_the_edge_without_neighbors += 1
        return disks_on_the_edge_without_neighbors

    def get_on_edge(self, board, color):
        places_on_edge = []
        for i in range(1, board.size - 1):
            if board.board[i][0].name == color:
                places_on_edge.append((i, 0))
            if board.board[0][i].name == color:
                places_on_edge.append((0, i))
            if board.board[i][7].name == color:
                places_on_edge.append((i, 7))
            if board.board[7][i].name == color:
                places_on_edge.append((7, i))
        return places_on_edge

    def get_number_of_disks_on_square(self, board, start, end, color):
        disks_on_edge = 0
        for i in range(1, board.size - 1):
            if board.board[i][start].name == color:
                disks_on_edge += 1
            if board.board[start][i].name == color:
                disks_on_edge += 1
            if board.board[i][end].name == color:
                disks_on_edge += 1
            if board.board[end][i].name == color:
                disks_on_edge += 1
        return disks_on_edge

    def get_pairs_on_edge(self, board, place_on_edge):
        """The function get a place on the edge and return as list his neighbors on the edge with
         different color (0-2 neighbors)"""
        opposite_neighbors_on_edge = self.get_opposite_neighbors_on_edge(board, place_on_edge)
        if board.board[place_on_edge[0]][place_on_edge[1]].name == "DARK":
            pairs = [(place_on_edge, neighbor) for neighbor in opposite_neighbors_on_edge]
        else:
            pairs = [(neighbor, place_on_edge) for neighbor in opposite_neighbors_on_edge]
        return pairs

    def get_opposite_neighbors_on_edge(self, board, place_on_edge):
        """the function get a place on the edge of the board (but not a corner), and returns its neighbors
         with opposite color that are also on the edge"""
        neighbors_on_edge = []
        if place_on_edge[0] == 0 or place_on_edge[0] == board.size:
            if board.board[place_on_edge[0]][place_on_edge[1] + 1].name == self.opposite_color(board.board[place_on_edge[0]][place_on_edge[1]].name):
                neighbors_on_edge.append((place_on_edge[0], place_on_edge[1] + 1))
            if board.board[place_on_edge[0]][place_on_edge[1] - 1].name == self.opposite_color(board.board[place_on_edge[0]][place_on_edge[1]].name):
                neighbors_on_edge.append((place_on_edge[0], place_on_edge[1] - 1))
        elif place_on_edge[1] == 0 or place_on_edge[1] == board.size:
            if board.board[place_on_edge[0] + 1][place_on_edge[1]].name == self.opposite_color(board.board[place_on_edge[0]][place_on_edge[1]].name):
                neighbors_on_edge.append((place_on_edge[0] + 1, place_on_edge[1]))
            if board.board[place_on_edge[0] - 1][place_on_edge[1]].name == self.opposite_color(board.board[place_on_edge[0]][place_on_edge[1]].name):
                neighbors_on_edge.append((place_on_edge[0] - 1, place_on_edge[1]))
        return neighbors_on_edge









