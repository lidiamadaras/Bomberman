import pygame

from bomb import Bomb
from bomberman import Bomberman
from gameSprite import Transparency
from wall import Wall
from box import Box
from bonus import Bonus


class Tile:
    """
    A class to represent the squared space on the map, which can contain several sprites at the same time
    """

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.sprites = []

    def add_sprite(self, sprite):
        """
        Adds the sprite to the sprites list
        :param sprite:
        :return:
        """
        self.sprites.append(sprite)

    def contains(self, sprite):
        """
        Checks if the tile contains some sprite
        :param sprite:
        :return:
        """
        return sprite in self.sprites

    def containsBonus(self):
        """
        Checks if there is a bonus on the tile
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Bonus):
                return True
        return False

    def getBonus(self):
        """
        Returns the bonus contained by the tile
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Bonus):
                return sprite
        return None

    def containsWall(self):
        """
        Checks if there is a wll on the tile
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Wall):
                return True
        return False

    def containsBox(self):
        """
        Checks if there is a box on the tile
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Box):
                return True
        return False

    def containsBomb(self):
        """
        Checks if there is a bomb on the tile
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Bomb):
                return True
        return False

    def containsObstacle(self):
        """
        Checks if there is an obstacle object for a bomberman or monster
        :return:
        """
        return self.containsWall() or self.containsBox() or self.containsBomb()

    def isFree(self):
        """
        Checks if the tile is empty
        :return:
        """
        return len(self.sprites) == 0

    def isFreeForBomberman(self, bomberman):
        """
        Checks if the tile is available for the bomberman to stand on
        :param bomberman:
        :return:
        """
        flag = True
        for sprite in self.sprites:
            if isinstance(sprite, Bomb):
                return not pygame.sprite.collide_rect(sprite, bomberman)
            if isinstance(sprite, Box):
                return not pygame.sprite.collide_rect(sprite, bomberman)
            if isinstance(sprite, Wall):
                return not pygame.sprite.collide_rect(sprite, bomberman)
        return flag

    def isFreeToStepOff(self):
        """
        Checks if the tile is available for the bomberman to stand right after stepping off the bomb or box
        :return:
        """
        flag = True
        for sprite in self.sprites:
            if isinstance(sprite, Box):
                return False
            if isinstance(sprite, Wall):
                return False
        return flag

    def freeToBomb(self):
        """
        Checks if the tile is suitable for bomb placement
        :return:
        """
        flag = True
        for sprite in self.sprites:
            if isinstance(sprite, Bomb):
                return False
        return flag

    def containsTransparency(self):
        """
        Checks if the tile has the flickering battle royale effect
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Transparency):
                return True
        return False

    def getTransparency(self):
        """
        Returns back the transparent wall preview
        :return:
        """
        for sprite in self.sprites:
            if isinstance(sprite, Transparency):
                return sprite
        return None
