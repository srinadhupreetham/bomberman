""" This module belongs to enemy functionalities """
from __future__ import print_function
import random
from person import Person


class Enemy(Person):  # inherits class person
    """ This class is to move enemy randomly """
    def __init__(self, x_pos, y_pos, lives, active):
        Person.__init__(self, x_pos, y_pos, lives)
        self.active = active

    def createenemy(self, board, char):
        """ Method to create enemy"""
        for i in range(4):
            for j in range(2):
                board[self.x_pos + j][self.y_pos + i] = char
        return board

    def generateenemy(self, board):
        """ Method to generate enemy """
        self.createenemy(board, 'E')
        return board

    def randommove(self, board, bom):
        """ Random movement of enemy """
        while True:
            i = random.randint(0, 3)    # geneartes random int to move enemy
            if i == 0:
                if board[self.x_pos - 2][self.y_pos] == ' ':
                    self.moveup(board, 0)
                elif board[self.x_pos - 2][self.y_pos] == 'B':
                    bom.lives -= 1   # bom_man dies
                    if bom.lives == 0:   # game quits
                        print('Game over')
                        exit()
                break
            elif i == 1:
                if board[self.x_pos + 2][self.y_pos] == ' ':
                    self.movedown(board, 0)
                elif board[self.x_pos + 2][self.y_pos] == 'B':
                    bom.lives -= 1
                    # print(bom.lives)
                    if bom.lives == 0:
                        print('Game over')
                        exit()
                break
            elif i == 2:
                if board[self.x_pos][self.y_pos - 4] == ' ':
                    self.moveleft(board, 0)
                elif board[self.x_pos][self.y_pos - 4] == 'B':
                    bom.lives -= 1
                    # print(bom.lives)
                    if bom.lives == 0:
                        print('Game over')
                        exit()
                break
            elif i == 3:
                if board[self.x_pos][self.y_pos + 4] == ' ':
                    self.moveright(board, 0)
                elif board[self.x_pos][self.y_pos + 4] == 'B':
                    bom.lives -= 1
                    # print(bom.lives)
                    if bom.lives == 0:
                        print('Game over')
                        exit()
                break
        return board
