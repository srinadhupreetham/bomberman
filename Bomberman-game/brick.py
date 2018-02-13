""" This class generates bricks """
import random

class Brick:
    """ birck class does some fucking thing """
    def __init__(self, num, x_size, y_size, b_x_size, b_y_size):
        self.num = num
        self.x_size = x_size
        self.y_size = y_size
        self.b_x_size = b_x_size
        self.b_y_size = b_y_size

    def generatebricks(self, board):
        """ This genraetes bricks on board those are breakable"""
        count = 0
        while True:
            i = random.randint(2, self.b_x_size - 4)
            j = random.randint(4, self.b_y_size - 8)
            temp_row = i % 2
            temp_column = j % 4
            i = i - temp_row        # gives exact location of vacancy
            j = j - temp_column
            if board[i][j] == ' ':
                if i == 2 and j == 8:  # brick should not be genrated
                    pass                # beside bom_man
                elif i == 4 and j == 4:
                    pass
                else:
                    count = count + 1
                    for row in range(self.y_size):
                        for col in range(self.x_size):
                            board[i + col][j + row] = '/'
            if count == self.num:
                break
        return board

    def destroybrick(self):
        """ we will not use this """
        pass
