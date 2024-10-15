import pygame

from bomberman import Bomberman


class Player:
    """
    A class to represent the current players, which keeps track of the player's
    number of victories in the rounds and the overall score
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.score = 0
        self.wins = 0
