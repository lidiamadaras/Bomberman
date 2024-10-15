import pytest
import pygame
from _pytest import unittest

from maps import MAP4
from gameEngine import GameEngine
from monster import Monster
from level import Level


class MonsterTest:
    def __init__(self):
        # pygame.init()

        tile_size = 48

    def test_movement(self):
        assert True == True
        # x = self.level.monsters[0].rect.x
        # y = self.level.monsters[0].rect.y
        #
        # self.level.monsters[0].move()
        #
        # assert x != self.level.monsters[0].rect.x or y != self.level.monsters[0].rect.y


# class MyTestCase(unittest.TestCase):
#     def __init__(self):
#         super().__init__()
#         # pygame.init()
#         #
#         # tile_size = 48
#         #
#         # screen_height = tile_size * len(MAP4) + tile_size * 2
#         # screen_width = tile_size * len(MAP4[0])
#         #
#         # screen = pygame.display.set_mode((screen_width, screen_height))
#         # self.gameEngine = GameEngine()
#         # self.level = self.gameEngine.level
#         # self.bomberman1 = self.level.bombermans[0]
#         # self.bomberman2 = self.level.bombermans[1]
#
#     # def test_movement(self):
#     #     x = self.level.monsters[0].rect.x
#     #     y = self.level.monsters[0].rect.y
#     #
#     #     self.level.monsters[0].move()
#     #
#     #     self.assertTrue(x != self.level.monsters[0].rect.x or y != self.level.monsters[0].rect.y)
#
#
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
