""" this module is plays a key role that is using all odules to play """
import time
import os
import random
import signal
from board import Board
from brick import Brick
from bomberman import Bomberman
from getchunix import GetchUnix
from enemy import Enemy
from bomb import Bomb
from alarmexception import AlarmException
EMB = Board(42, 84, 2, 4)         # creates object b od class Board
BNE = EMB.createboard()
BNE = EMB.buildrigidboard(BNE)        # Builds borders of board with walls
BNE = EMB.buildmiddlewalls(BNE)       # symmetric spaces of board with walls
B = Bomberman(2, 4, 3, 0)     # bom is our object bomberman
BNE = B.generatebomberman(BNE)
C = Brick(30, 2, 4, 42, 84)
BNE = C.generatebricks(BNE)         # Creates bricks(breakable) randomly on board
EMB.enemies = [0] * 6             # Creates list of enemies
G = GetchUnix()


def alarmhandler(signum, frame):
    """ this method controls time and char relation """
    signum = signum
    frame = frame
    raise AlarmException


def input_to(timeout=1):  # time after which enemies move automatically
    """ this method is to get input """
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.alarm(timeout)
    try:
        text = G()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


for tem in range(6):
    pasttime = time.time()             # calc time when this is evaluated
    while True:
        x = random.randint(2, EMB.rows - 4)
        y = random.randint(4, EMB.columns - 8)
        jtem = x % 2
        x = x - jtem
        jtem = y % 4
        y = y - jtem
        if x == 2 and y == 8:    # we should not GenerateEnemy beside Bomberman
            pass
        elif x == 4 and y == 4:
            pass
        elif BNE[x][y] == ' ':
            break
    EMB.enemies[tem] = Enemy(x, y, 3, 1)
    BNE = EMB.enemies[tem].generateenemy(BNE)       # Populate enemies on board


def printboard(BNE):
    """ this method prints board """
    row = 0
    col = 0
    for temp in BNE:
        row += 1
        for jtemp in temp:
            jtemp = jtemp
            col += 1
            print(BNE[row - 1][col - 1], end='')
        col = 0
        print(end='\n')  # to get contents printed on new line end should be \n
    print('Score:' + "\t", end='')
    print(B.score)
    presenttime = time.time()           # calc present time
    diff = 180 - int(presenttime - pasttime)     # decrease time from 30
    print('Time left : ', end='')                # using present and past times
    print(diff)
    if diff == 0:
        print('game over')
        exit()                          # time is up (so quit)
    print('Number of lives: ', end='')
    print(B.lives)
printboard(BNE)

def printboard1():
    """ this method prints board """
    row = 0
    col = 0
    for temp1 in BNE:
        row += 1
        for jtemp1 in temp1:
            jtemp1 = jtemp1
            col += 1
            if BNE[row - 1][col - 1] == 'e':    # replace 'e' with ' '
                BNE[row - 1][col - 1] = ' '     # after explosion
            print(BNE[row - 1][col - 1], end='')
        col = 0
        print(end='\n')
    print('Score:' + "\t", end='')
    print(B.score)
    presenttime = time.time()
    diff = 180 - int(presenttime - pasttime)
    print('Time left : ', end='')
    print(diff)
    if diff == 0:
        print('game over')
        exit()
    print('Number of lives: ', end='')
    print(B.lives)


def startgame(BNE):
    """ this method starts the game """
    nextstep = time.time() + 1      # value to make enemies move automatically
    flag = 0                        # bomb is not there on the board
    B.score = 0
    while True:
        inp = input_to()
        if inp == 'q':
            break
        if inp == 'w':
            BNE = B.moveup(BNE, 1)
            os.system('clear')      # clears screen or refreshes
            printboard(BNE)
        if inp == 's':
            BNE = B.movedown(BNE, 1)
            os.system('clear')
            printboard(BNE)
        if inp == 'a':
            BNE = B.moveleft(BNE, 1)
            os.system('clear')
            printboard(BNE)
        if inp == 'd':
            BNE = B.moveright(BNE, 1)
            os.system('clear')
            printboard(BNE)
        if flag != 1:               # bomb is not placed
            if inp == 'b':
                boom = Bomb(B.x_pos, B.y_pos, 1)
                if flag == 0:
                    bomb_start = time.time()
                    BNE = boom.placebomb(BNE)
                    flag = 1
                    os.system('clear')
                printboard(BNE)
        if flag == 1:                  # bomb is there on board
            if time.time() - bomb_start > 3:   # if it has been more than 3 sec
                BNE = boom.explode(BNE, EMB, B)     # after placing bomb
                flag = 0
                os.system('clear')
                printboard(BNE)
                time.sleep(0.3)        # shows board with e's for 0.3 sec
                os.system('clear')
                printboard1()
        if time.time() >= nextstep:
            nextstep = nextstep + 1
            for i in EMB.enemies:
                BNE = i.randommove(BNE, B)
            os.system('clear')
            printboard(BNE)
startgame(BNE)
