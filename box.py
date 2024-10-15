from gameSprite import GameSprite
from bonus import *
import random
import pygame


class Box(GameSprite):
    """
    A class to represent the box either loaded to the map from the maps file or placed by the
    bomberman by the obstacle power up
    """

    tile_size = 48
    # Some bonuses are more frequent than others:
    #              (NumberOfBombs)  (BlastRange)   (RollerSkate)     (Ghost)(Obstacle)          [ImmediatePlacing]
    #                       6x             5x             3x            2x    2x                        1x
    bonusOptions = [
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        2,
        3,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        7,
        8,
        8,
        9,
        9,
        10,
    ]
    #                                                1x           2x               3x        2x    2x
    #                                           (Detonator)(Invincibility)   [SlowDown][ShortRange][NoBombs]
    # bonusOptions = [5]
    bombImage = pygame.image.load("img/bombPowerUp.png")
    bombPowerUpImage = pygame.transform.scale(bombImage, (tile_size, tile_size))
    skull = pygame.image.load("img/skull.png")
    skullImage = pygame.transform.scale(skull, (tile_size, tile_size))
    plant = pygame.image.load("img/plant.png")
    plantImage = pygame.transform.scale(plant, (tile_size, tile_size))
    ghost = pygame.image.load("img/ghost.png")
    ghostImage = pygame.transform.scale(ghost, (tile_size, tile_size))
    obstacle = pygame.image.load("img/obstacle.png")
    obstacleImage = pygame.transform.scale(obstacle, (tile_size, tile_size))
    rollerSkate = pygame.image.load("img/rollerSkate.png")
    rollerSkateImage = pygame.transform.scale(rollerSkate, (tile_size, tile_size))
    shield = pygame.image.load("img/shield.png")
    shieldImage = pygame.transform.scale(shield, (tile_size, tile_size))
    detonator = pygame.image.load("img/detonator.png")
    detonatorImage = pygame.transform.scale(detonator, (tile_size, tile_size))

    def __init__(self, level, i, j, x, y, hasBonus, image):
        """
        With 2/3 probability contains the bonus
        :param level:
        :param i:
        :param j:
        :param x:
        :param y:
        :param hasBonus: Determined when loading from the maps file (is always False when placed by the bomberman)
        :param image:
        """
        super().__init__(x, y, i, j, image)
        self.level = level
        self.hasBonus = hasBonus  # bool value that we pass a parameter, it will decide of there is a bonus inside this box or not, it will be decided randomly
        if self.hasBonus:
            rand = random.randint(0, len(Box.bonusOptions) - 1)
            # POWER UPS
            if Box.bonusOptions[rand] == 0:
                self.bonus = NumberOfBombsPowerUp(
                    self.i, self.j, x, y, Box.bombPowerUpImage
                )
            if Box.bonusOptions[rand] == 1:
                self.bonus = BlastRangePowerUp(self.i, self.j, x, y, Box.plantImage)
            if Box.bonusOptions[rand] == 2:
                self.bonus = DetonatorPowerUp(self.i, self.j, x, y, Box.detonatorImage)
            if Box.bonusOptions[rand] == 3:
                self.bonus = RollerSkatePowerUp(
                    self.i, self.j, x, y, Box.rollerSkateImage
                )
            if Box.bonusOptions[rand] == 4:
                self.bonus = InvincibilityPowerUp(self.i, self.j, x, y, Box.shieldImage)
            if Box.bonusOptions[rand] == 5:
                self.bonus = GhostPowerUp(self.i, self.j, x, y, Box.ghostImage)
            if Box.bonusOptions[rand] == 6:
                self.bonus = ObstaclePowerUp(self.i, self.j, x, y, Box.obstacleImage)
            # CURSES
            # All of them have the same image
            if Box.bonusOptions[rand] == 7:
                self.bonus = SlowDownCurse(self.i, self.j, x, y)
            if Box.bonusOptions[rand] == 8:
                self.bonus = ShortRangeCurse(self.i, self.j, x, y)
            if Box.bonusOptions[rand] == 9:
                self.bonus = NoBombsCurse(self.i, self.j, x, y)
            if Box.bonusOptions[rand] == 10:
                self.bonus = ImmediatePlacingCurse(self.i, self.j, x, y)

    def blowUp(self):
        """
        Calls the appropriate function in the level to animate the blowing up
        :return:
        """
        self.level.blowUpBox(self)

    def absorbExplosion(self):
        """
        In case of explosion blows up
        :return:
        """
        self.blowUp()
