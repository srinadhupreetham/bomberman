""" This module has movement fuctions of bomberman and enemy """
from __future__ import print_function

class Person:
    """ This class has movement fuctions of bomberman and enemy """
    def __init__(self, x_pos, y_pos, lives):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.lives = lives

    def moveright(self, board, typ):  # here if typ is 1 then person is bomberman
        """ This method is to move person to right """
        if board[self.x_pos][self.y_pos + 4] == ' ':
            if board[self.x_pos][self.y_pos] == '0':  # if prev pos is on bomb
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i + 4] = 'B'
            else:
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i], \
                        board[self.x_pos + j][self.y_pos + i + 4] = \
                        board[self.x_pos + j][self.y_pos + i + 4], \
                        board[self.x_pos + j][self.y_pos + i]
            self.y_pos = self.y_pos + 4
        if typ == 1 and board[self.x_pos][self.y_pos + 4] == 'E':  # bom_man dies
            self.lives -= 1
            if self.lives == 0:  # game quits sice lives are 0
                print('Game over')
                exit()
        return board

    def moveleft(self, board, typ):
        """ This method is to move person to left """
        if board[self.x_pos][self.y_pos - 4] == ' ':
            if board[self.x_pos][self.y_pos] == '0':  # if prev pos is on bomb
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i - 4] = 'B'
            else:
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i], \
                        board[self.x_pos + j][self.y_pos + i - 4] = \
                        board[self.x_pos + j][self.y_pos + i - 4], \
                        board[self.x_pos + j][self.y_pos + i]
            self.y_pos = self.y_pos - 4
        if typ == 1 and board[self.x_pos][self.y_pos - 4] == 'E':
            self.lives -= 1
            if self.lives == 0:
                print('Game over')
                exit()
        return board

    def moveup(self, board, typ):
        """ This method is to move person to up """
        if board[self.x_pos - 2][self.y_pos] == ' ':
            if board[self.x_pos][self.y_pos] == '0':  # if prev pos is on bomb
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j - 2][self.y_pos + i] = 'B'
            else:
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i], \
                        board[self.x_pos + j - 2][self.y_pos + i] = \
                        board[self.x_pos + j - 2][self.y_pos + i], \
                        board[self.x_pos + j][self.y_pos + i]
            self.x_pos = self.x_pos - 2
        if typ == 1 and board[self.x_pos - 2][self.y_pos] == 'E':
            self.lives -= 1
            if self.lives == 0:
                print('game over')
                exit()
        return board

    def movedown(self, board, typ):
        """ This method is to move person to down """
        if board[self.x_pos + 2][self.y_pos] == ' ':
            if board[self.x_pos][self.y_pos] == '0':  # if prev pos is on bomb
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j + 2][self.y_pos + i] = 'B'
            else:
                for i in range(4):
                    for j in range(2):
                        board[self.x_pos + j][self.y_pos + i], \
                        board[self.x_pos + j + 2][self.y_pos + i] = \
                        board[self.x_pos + j + 2][self.y_pos + i], \
                        board[self.x_pos + j][self.y_pos + i]
            self.x_pos = self.x_pos + 2
        if typ == 1 and board[self.x_pos + 2][self.y_pos] == 'E':
            self.lives -= 1
            if self.lives == 0:
                print('game over')
                exit()
        return board
