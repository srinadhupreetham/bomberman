""" This module consists of every functionalities taht involve bomb"""
from __future__ import print_function


class Bomb:
    """ This class bomb consists of functaionalities related to bombs like removing bomberman
     bricks"""
    def __init__(self, x_ind, y_ind, bombcount):
        self.x_ind = x_ind
        self.y_ind = y_ind
        self.bombcount = bombcount

    def placebomb(self, board):  # places bomb (activated)
        """ this method is to place a bomb with given co ordinates"""
        for i in range(4):
            for j in range(2):
                board[self.x_ind + j][self.y_ind + i] = '0'
        return board
#    def VacateSpace(self,x_pos,y_pos,X):

    def explode(self, board, boa, bom):
        """ This method is used to explode bombs and clear near by areas if possible"""
        if self.x_ind == bom.x_pos and self.y_ind == bom.y_pos:
            bom.lives -= 1
            if bom.lives == 0:
                print("game over")
                exit()
        list1 = [self.x_ind - 2, self.x_ind + 2]  # blocks up and down to bomb
        list2 = [self.y_ind - 4, self.y_ind + 4]  # blocks beside bomb
        for i in list1:
            if board[i][self.y_ind] == ' ':
                for j in range(4):
                    board[i][self.y_ind + j] = 'e'
                    board[i + 1][self.y_ind + j] = 'e'
            if board[i][self.y_ind] == '/':
                bom.score = bom.score + 20
                for j in range(4):
                    board[i][self.y_ind + j] = 'e'
                    board[i + 1][self.y_ind + j] = 'e'
            if board[i][self.y_ind] == 'E':
                bom.score += 100
                for j in boa.enemies:
                    if i == j.x_pos and self.y_ind == j.y_pos:
                        boa.enemies.remove(j)
                for j in range(4):
                    board[i][self.y_ind+j] = 'e'
                    board[i+1][self.y_ind+j] = 'e'
            if board[i][self.y_ind] == 'B':
                bom.lives -= 1
                if bom.lives == 0:
                    print("game over")
                    exit()
        for i in list2:
            if board[self.x_ind][i] == ' ':
                for j in range(4):
                    board[self.x_ind][i + j] = 'e'
                    board[self.x_ind+1][i + j] = 'e'
            if board[self.x_ind][i] == '/':
                bom.score = bom.score + 20
                for j in range(4):
                    board[self.x_ind][i + j] = 'e'
                    board[self.x_ind+1][i + j] = 'e'
            if board[self.x_ind][i] == 'E':
                bom.score += 100
                for j in boa.enemies:
                    if i == j.y_pos and self.x_ind == j.x_pos:
                        boa.enemies.remove(j)
                for j in range(4):
                    board[self.x_ind][i + j] = 'e'
                    board[self.x_ind+1][i + j] = 'e'
            if board[self.x_ind][i] == 'B':
                bom.lives -= 1
                if bom.lives == 0:
                    print("game over")
                    exit()
        for i in range(4):
            for j in range(2):
                board[self.x_ind + j][self.y_ind + i] = 'e'
        return board
