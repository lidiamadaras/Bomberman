import pygame
from gameSprite import GameSprite
import level

tile_size = 48
redBomb = pygame.image.load("img/redBombBig.png")
# redBomb = pygame.transform.scale(red, (50, 50))
purpleBomb = pygame.image.load("img/purpleBombBig.png")


# purpleBomb = pygame.transform.scale(purple, (50, 50))
class Bomb(GameSprite):
    """
    A class to represent the bomb object, which is GameSprite as well
    """

    def __init__(self, level, id, i, j, x, y, blastRange, image, image2):
        super().__init__(x, y, i, j, image)
        self.initTime = pygame.time.get_ticks()
        self.deathTime = pygame.time.get_ticks()
        self.timer = 5000
        self.level = level
        self.blastRange = blastRange
        self.isExploding = False
        self.isDetonated = False
        self.leftExplosion = True
        self.rightExplosion = True
        self.upExplosion = True
        self.downExplosion = True
        self.isReturned = False
        self.image1 = image
        self.image2 = image2
        self.imageCounter1 = 56
        self.imageCounter2 = 14
        self.expNum = 0
        self.id = id

    def explode(self):
        """
        Calls the appropriate function in the level class to animate the bomb explosion and remove it
        :return:
        """
        self.level.explodeBomb(self)

    def absorbExplosion(self):
        """
        In case of bombs chain explosion causes the bomb to explode immediately
        :return:
        """
        if not self.isExploding:
            self.initTime = pygame.time.get_ticks() - 5000
