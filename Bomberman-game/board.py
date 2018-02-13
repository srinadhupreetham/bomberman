""" THis module is realeted to board basic one that appers without
people and bombs """
class Board:
    """ THis class prints the board and populates blocks in the board"""
    def __init__(self, rows, columns, x_size, y_size):
        self.rows = rows
        self.columns = columns
        self.x_size = x_size
        self.y_size = y_size
        self.enemies = []

    def createboard(self):
        """ This method creates empty board """
        board = [[' ' for _ in range(self.columns)]for _ in range(self.rows)]
        return board

    def createwallblock(self, board, x_ind, y_ind, char):
        """ This is a general method to create Wall blocks on empty board """
        for i in range(self.y_size):
            for j in range(self.x_size):
                board[x_ind + j][y_ind + i] = char
        return board

    def buildrigidboard(self, board):   # populate border walls
        """ This method populates Wall blocks on empty board (boundary)"""
        row = self.rows - (self.rows % 2)
        col = self.columns - (self.columns % 4)
        for i in range(int(col/4)):
            self.createwallblock(board, 0, 4 * i, 'X')
            self.createwallblock(board, row - 2, 4 * i, 'X')
        for i in range(int(row/2 - 2)):
            self.createwallblock(board, 2*i + 2, 0, 'X')
            self.createwallblock(board, 2*i + 2, col - 4, 'X')
        return board

    def buildmiddlewalls(self, board):  # populate symmetric middle walls
        """ This method populates Wall blocks on empty board (inner board)"""
        row = self.rows - (self.rows % 2)
        col = self.columns - (self.columns % 4)
        for i in range(1, int((row - 6) / 4 + 1)):
            for j in range(1, int((col - 12) / 8 + 1)):
                self.createwallblock(board, 4*i, 8*j, 'X')
        return board
