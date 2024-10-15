import pytest
import pygame
from maps import MAP4
from gameEngine import GameEngine
from bonus import *
from explosion import Explosion


class Testing:
    """
    A single test class that runs
    """

    def restart(self):
        """
        Recreates the initial test staging state
        :return:
        """
        pygame.init()

        tile_size = 48

        screen_height = tile_size * len(MAP4) + tile_size * 2
        screen_width = tile_size * len(MAP4[0])

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.gameEngine = GameEngine()
        self.level = self.gameEngine.level
        self.bomberman1 = self.level.bombermans[0]
        self.bomberman2 = self.level.bombermans[1]

    def test_movement(self):
        """
        Testing monster's movement by checking its coordinates after the single move() call
        :return:
        """
        self.restart()
        x = self.level.monsters[0].rect.x
        y = self.level.monsters[0].rect.y

        self.level.monsters[0].move()

        assert x != self.level.monsters[0].rect.x or y != self.level.monsters[0].rect.y

    def test_bomberman_movement(self):
        """
        Testing bomberman's movement by comparing the bomberman's x-coordinate after moving right
        :return:
        """
        self.restart()
        x = self.bomberman1.rect.x
        self.bomberman1.moveRight()
        assert x != self.bomberman1.rect.x

    def test_bomberman_long_movement(self):
        """
        Testing bomberman's movement by comparing the bomberman's j-index after 25 moves to the right
        :return:
        """
        self.restart()
        j = self.bomberman1.j
        for i in range(25):
            self.bomberman1.moveRight()
        assert j != self.bomberman1.j

    def test_bomberman_overflow_movement(self):
        """
        Testing bomberman's auto movement when there's an overflow in the x-coordinate
        :return:
        """
        self.restart()
        j = self.bomberman1.j
        for i in range(13):
            self.bomberman1.moveRight()
        assert j != self.bomberman1.j

    def test_collecting_bonus(self):
        """
        Testing bomberman's bonus-coolecting ability
        :return:
        """
        self.restart()
        bonus = SlowDownCurse(
            self.bomberman1.i,
            self.bomberman1.j + 1,
            self.bomberman1.rect.x + 48,
            self.bomberman1.rect.y,
        )
        self.level.tiles[self.bomberman1.i][self.bomberman1.j + 1].sprites.append(bonus)
        for i in range(13):
            self.bomberman1.moveRight()
        self.level.refresh()
        assert len(self.bomberman1.bonuses) == 0

    def test_monster_death(self):
        """
        Testing monster's willingness to die when it should happen
        :return:
        """
        self.restart()
        monster = self.level.monsters[0]
        # explosion = Explosion(0, monster.i, monster.j, )
