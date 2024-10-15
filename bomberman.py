import pygame

from box import Box
from gameSprite import GameSprite
from bomb import Bomb


tile_size = 48
redBomb = pygame.image.load("img/redBombBig.png")
purpleBomb = pygame.image.load("img/purpleBombBig.png")
redBombSmall = pygame.image.load("img/redBombSmall.png")
purpleBombSmall = pygame.image.load("img/purpleBombSmall.png")
redBombImage = pygame.transform.scale(redBomb, (tile_size, tile_size))
purpleBombImage = pygame.transform.scale(purpleBomb, (tile_size, tile_size))
redBombSmallImage = pygame.transform.scale(redBombSmall, (tile_size, tile_size))
purpleBombSmallImage = pygame.transform.scale(purpleBombSmall, (tile_size, tile_size))
grave = pygame.image.load("img/grave.png")
graveImage = pygame.transform.scale(grave, (tile_size, tile_size))

box = pygame.image.load("img/box.png")
boxImage = pygame.transform.scale(box, (tile_size, tile_size))


class Bomberman(GameSprite):
    """
    A class to represent a bomberman on the current round of the current game
    """

    def __init__(self, id, level, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

        self.level = level
        self.id = id
        if id == 1:
            self.image = pygame.transform.scale(
                pygame.image.load("img/player1.png"), (tile_size, tile_size)
            )
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("img/player2.png"), (tile_size, tile_size)
            )

        self.vel = 2
        self.bombsNum = 1
        self.bombs = []
        self.blastRange = 3
        # advanced power ups
        self.ghost = False
        self.detonator = False
        self.isInvincible = False
        self.obstaclesNum = 0
        self.obstacles = []

        # curses
        self.noBombs = False
        self.immediateBombs = False

        self.up = True
        self.down = True
        self.left = True
        self.right = True
        self.overflowLeft = False
        self.overflowRight = False
        self.overflowUp = False
        self.overflowDown = False
        self.isAlive = True
        self.bonuses = {}

    def moveLeft(self):
        """
        Moves the bomberman left by the current velocity
        :return:
        """
        if self.rect.x >= self.vel and self.left:
            self.rect.x -= self.vel
            self.removeFromTile()
            self.j = (self.rect.x + 24) // tile_size
            self.insertToTile()
            if self.rect.x % tile_size < 32:
                self.overflowLeft = True
            if self.rect.x % tile_size == 0:
                self.overflowLeft = False

    def moveRight(self):
        """
        Moves the bomberman right by the current velocity
        :return:
        """
        if (
            self.rect.x < self.level.col_count * tile_size - tile_size
            and self.right
            and (
                not self.rect.x % tile_size == 0
                or not self.level.tiles[self.i][self.j + 1].containsObstacle()
                or self.ghost
            )
        ):
            self.rect.x += self.vel
            self.removeFromTile()
            self.j = (self.rect.x + 24) // tile_size
            self.insertToTile()
            if self.rect.x % tile_size > 16:
                self.overflowRight = True
            if self.rect.x % tile_size == 0:
                self.overflowRight = False

    def moveUp(self):
        """
        Moves the bomberman up by the current velocity
        :return:
        """
        if self.rect.y > 0 and self.up:
            self.rect.y -= self.vel
            self.removeFromTile()
            self.i = (self.rect.y + 24) // tile_size
            self.insertToTile()
            if self.rect.y % tile_size < 32:
                self.overflowUp = True
            if self.rect.y % tile_size == 0:
                self.overflowUp = False

    def moveDown(self):
        """
        Moves the bomberman down by the current velocity
        :return:
        """
        if (
            self.rect.y < self.level.row_count * tile_size - tile_size
            and self.down
            and (
                not self.rect.y % tile_size == 0
                or not self.level.tiles[self.i + 1][self.j].containsObstacle()
                or self.ghost
            )
        ):
            self.rect.y += self.vel
            self.removeFromTile()
            self.i = (self.rect.y + 24) // tile_size
            self.insertToTile()
            if self.rect.y % tile_size < 16:
                self.overflowDown = True
            if self.rect.y % tile_size == 0:
                self.overflowDown = False

    def removeFromTile(self):
        """
        Removes the bomberman from the board in order to "teleport" him
        :return:
        """
        self.level.tiles[self.i][self.j].sprites.remove(self)

    def insertToTile(self):
        """
        Returns the bomberman back to the board
        :return:
        """
        self.level.tiles[self.i][self.j].sprites.append(self)

    def placeBomb(self):
        """
        Creates the new bomb and places it on the same tile bomberman is standing at
        :return:
        """
        if self.bombsNum > 0 and self.level.tiles[self.i][self.j].freeToBomb():
            if self.id == 0:
                bomb = Bomb(
                    self.level,
                    self.id,
                    self.i,
                    self.j,
                    self.j * tile_size,
                    self.i * tile_size,
                    self.blastRange,
                    redBomb,
                    redBombSmall,
                )
            if self.id == 1:
                bomb = Bomb(
                    self.level,
                    self.id,
                    self.i,
                    self.j,
                    self.j * tile_size,
                    self.i * tile_size,
                    self.blastRange,
                    purpleBomb,
                    purpleBombSmall,
                )
            self.bombs.append(bomb)
            self.level.addBomb(bomb)
            self.bombsNum -= 1

    def placeObstacle(self):
        """
        Creates the new box and places it on the same tile bomberman is standing at
        :return:
        """
        if self.obstaclesNum > 0 and self.level.tiles[self.i][self.j].freeToBomb():
            if self.id == 0:
                bomb = Bomb(
                    self.level,
                    self.id,
                    self.i,
                    self.j,
                    self.j * tile_size,
                    self.i * tile_size,
                    self.blastRange,
                    redBomb,
                    redBombSmall,
                )
            if self.id == 1:
                bomb = Bomb(
                    self.level,
                    self.id,
                    self.i,
                    self.j,
                    self.j * tile_size,
                    self.i * tile_size,
                    self.blastRange,
                    purpleBomb,
                    purpleBombSmall,
                )
            box = Box(
                self.level,
                self.i,
                self.j,
                self.j * tile_size,
                self.i * tile_size,
                False,
                boxImage,
            )

            self.level.addObstacle(box)
            self.obstacles.append(box)
            self.obstaclesNum -= 1

    def die(self):
        """
        Makes the bomberman dead and replaces its image by the grave image
        :return:
        """
        if not self.isInvincible:
            self.isAlive = False
            self.image = graveImage

    def absorbExplosion(self):
        """
        In case of encountering an explosion makes the bomberman dead
        :return:
        """
        self.die()
