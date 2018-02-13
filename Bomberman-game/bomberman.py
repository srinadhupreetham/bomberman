""" this module is realted to creation of bomberman object"""
from person import Person


class Bomberman(Person):
    """ this is a child of parent class realted to bomberman """
    def __init__(self, x_pos, y_pos, lives, score):
        Person.__init__(self, x_pos, y_pos, lives)
        self.score = score

    def createperson(self, board, x_ind, y_ind, char):
        """ this creates person on the board """
        self = self
        for i in range(4):
            for j in range(2):
                board[x_ind + j][y_ind + i] = char
        return board

    def generatebomberman(self, board):
        """ this cslls craeting bomb fucntion with needed char """
        self.createperson(board, self.x_pos, self.y_pos, 'B')
        return board
