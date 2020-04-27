from disk import Disk

class Board:
    space = '-+' + '---+' * 8
    title = "  | a | b | c | d | e | f | g | h | \n"
    disk_display = {Disk.NONE : "   |", Disk.LIGHT : ' O |', Disk.DARK: ' X |'}

    def __init__(self, size):
        self.size = size
        self.start_board()

    def start_board(self):
        self.board = [[Disk.NONE for i in range(self.size)] for j in range(8)]
        self.board[self.size // 2][self.size // 2] = Disk.DARK
        self.board[self.size // 2 - 1][self.size // 2 - 1] = Disk.DARK
        self.board[self.size // 2 -1][self.size // 2] = Disk.LIGHT
        self.board[self.size // 2][self.size // 2 - 1] = Disk.LIGHT


    def __str__(self):
        print(self.title, self.space)
        for i, line in enumerate(self.board):
            print(f"{i} |", end = "")
            for j, disk in enumerate(line):
                print(self.disk_display[disk], end="")
            #print()
            print("\n", self.space)
        return ""

    def if_space_empty(self, place):
        #print(self.board[place[0]][place[1]].name)
        if self.board[place[0]][place[1]].name != "NONE":
            return False
        else:
            return True


    def get_neighbors(self, place):
        neighbors = []
        if self.in_board((place[0] - 1, place[1])):
            neighbors.append([(place[0] - 1, place[1]), self.board[place[0] - 1][place[1]]])
        if self.in_board((place[0] - 1, place[1] - 1)):
            neighbors.append([(place[0] - 1, place[1] - 1), self.board[place[0] - 1][place[1] - 1]])
        if self.in_board((place[0] - 1, place[1] + 1)):
            neighbors.append([(place[0] - 1, place[1] + 1), self.board[place[0] - 1][place[1] + 1]])
        if self.in_board((place[0], place[1] - 1)):
            neighbors.append([(place[0], place[1] - 1), self.board[place[0]][place[1] - 1]])
        if self.in_board((place[0], place[1] + 1)):
            neighbors.append([(place[0], place[1] + 1), self.board[place[0]][place[1] + 1]])
        if self.in_board((place[0] + 1, place[1] - 1)):
            neighbors.append([(place[0] + 1, place[1] - 1), self.board[place[0] + 1][place[1] - 1]])
        if self.in_board((place[0] + 1, place[1])):
            neighbors.append([(place[0] + 1, place[1]), self.board[place[0] + 1][place[1]]])
        if self.in_board((place[0] + 1, place[1] + 1)):
            neighbors.append([(place[0] + 1, place[1] + 1), self.board[place[0] + 1][place[1] + 1]])
        return neighbors

    def find_2_different(self):
        """return a list of tuples that contain all pairs of locations of DARK disk next to LIGHT"""
        darks = {(i, j) for i, line in enumerate(self.board) for j, disk in enumerate(line) if disk.name == "DARK"}
        different_pairs = [(dark, neighbor[0]) for dark in darks for neighbor in \
                           self.get_neighbors(dark) if neighbor[1].name == "LIGHT"]
        return different_pairs

    def in_board(self, place):
        if place[0] >= 0 and place[0] < self.size and place[1] >= 0 and place[1] < self.size:
            return True
        return False





