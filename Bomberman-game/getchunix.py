""" module has getchar unix class for getting characters"""
from __future__ import print_function
import sys
import tty
import termios


class GetchUnix:
    """ this class is to get continuous char  """
    def __init__(self):
        self = self

    def __call__(self):
        fds = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fds)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fds, termios.TCSADRAIN, old_settings)
        return char

    def getcharacter(self):
        """ this does nothing """
        pass

    def unix(self):
        """ this does nothing """
        pass
        