import pygame
import random

from gameSprite import GameSprite

tile_size = 48


class Monster(GameSprite):
    """
    A class to represent a monster object, which is GameSprite as well
    """

    skull = pygame.image.load("img/skull.png")
    skullImage = pygame.transform.scale(skull, (tile_size, tile_size))

    def __init__(self, level, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

        self.vel = 1
        self.i = i
        self.j = j
        self.isAlive = True
        self.level = level
        self.direction = 0
        self.firstRun = True
        self.deathTime = pygame.time.get_ticks()

    def moveLeft(self):
        """
        Moves a monster left by a unit velocity
        :return:
        """
        if self.rect.x > 0:
            self.rect.x -= self.vel
            self.removeFromTile()
            self.j = (self.rect.x + 24) // tile_size
            self.insertToTile()

    def moveRight(self):
        """
        Moves a monster right by a unit velocity
        :return:
        """
        if self.rect.x < self.level.col_count * tile_size - tile_size:
            self.rect.x += self.vel
            self.removeFromTile()
            self.j = self.rect.x // tile_size
            self.insertToTile()

    def moveUp(self):
        """
        Moves a monster up by a unit velocity
        :return:
        """
        if self.rect.y > 0:
            self.rect.y -= self.vel
            self.removeFromTile()
            self.i = (self.rect.y + 24) // tile_size
            self.insertToTile()

    def moveDown(self):
        """
        Moves a monster down by a unit velocity
        :return:
        """
        if self.rect.y < self.level.row_count * tile_size - tile_size:
            self.rect.y += self.vel
            self.removeFromTile()
            self.i = self.rect.y // tile_size
            self.insertToTile()

    def removeFromTile(self):
        """
        Removes the monster from the board in order to "teleport" it
        :return:
        """
        self.level.tiles[self.i][self.j].sprites.remove(self)

    def insertToTile(self):
        """
        Returns the monster back to the board
        :return:
        """
        self.level.tiles[self.i][self.j].sprites.append(self)

    def move(self):
        """
        Moves the monster in a direction which is determined by the other functions
        :return:
        """
        if self.isAlive:
            if self.firstRun:
                self.firstRun = False
                self.changeDirection()
                print(self.direction)
            if self.shouldChangeDirection():
                self.changeDirection()
            if self.direction == 0:
                self.moveUp()
            elif self.direction == 1:
                self.moveLeft()
            elif self.direction == 2:
                self.moveDown()
            elif self.direction == 3:
                self.moveRight()
            else:
                print("no free directions for monster")

    def changeDirection(self):
        """
        Updates the available directions and occasionally changes the direction of the monster
        :return:
        """
        availableDirections = self.__availableDirections()
        if len(availableDirections) == 1:
            self.direction = availableDirections[0]
            return
        if len(availableDirections) == 0:
            self.direction = 5
            return
        self.direction = availableDirections[
            random.randint(0, len(availableDirections) - 1)
        ]

    def shouldChangeDirection(self):
        """
        Decides whether to change monster's direction or not
        :return:
        """
        return not self.direction in self.__availableDirections()

    def __availableDirections(self):
        """
        Determines the possible directions for the monster
        :return:
        """
        availableDirections = []
        try:
            if self.level.tiles[self.i - 1][self.j].isFreeForBomberman(self):
                availableDirections.append(0)
            if self.level.tiles[self.i][self.j - 1].isFreeForBomberman(self):
                availableDirections.append(1)
            if self.level.tiles[self.i + 1][self.j].isFreeForBomberman(self):
                availableDirections.append(2)
            if self.level.tiles[self.i][self.j + 1].isFreeForBomberman(self):
                availableDirections.append(3)
        except:
            print("monster is out of bounds")
            return []
        return availableDirections

    # TODO: Implement this method

    def absorbExplosion(self):
        pass

    def die(self, id):
        """
        Makes the monster dead, animates it and adds score to the player, whose bomb killed the monster
        :param id:
        :return:
        """
        if self.isAlive:
            self.isAlive = False
            self.deathTime = pygame.time.get_ticks()
            self.image = Monster.skullImage
            if id == 0:
                self.level.player1.score += 100
            if id == 1:
                self.level.player2.score += 100
