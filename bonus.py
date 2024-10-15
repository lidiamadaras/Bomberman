import pygame
from gameSprite import GameSprite

tile_size = 48
skull = pygame.image.load("img/skull.png")
skullImage = pygame.transform.scale(skull, (tile_size, tile_size))


class Bonus(GameSprite):
    """
    Base class of the bonuses that introduces 2 bonus-related functions to GameSprite object
    """

    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        """
        Applies bonus effects to bomberman
        :param bomberman:
        :return:
        """
        pass

    def cancelBonus(self, bomberman):
        """
        For timed bonuses only: cancels the effect of the bonus on bomberman
        :param bomberman:
        :return:
        """
        pass


class PowerUp(Bonus):
    # The constructor requires the image
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)


class Curse(Bonus):
    # The constructor requires the image, but each of the child classes will have the same image

    def __init__(self, i, j, x, y):
        super().__init__(x, y, i, j, skullImage)


# all the powerups and curses here:
# POWERUPS:

# THE TWO BASIC POWERUPS FROM EXERCISE DESCRIPTION:


class NumberOfBombsPowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.bombsNum += 1


class BlastRangePowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.blastRange += 1


# REST OF THE EXTRA POWERUPS:


class DetonatorPowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.detonator = True


class RollerSkatePowerUp(PowerUp):

    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.vel = 3
        bomberman.rect.x -= bomberman.rect.x % 3
        bomberman.rect.y -= bomberman.rect.y % 3
        if "rollerSkate" not in bomberman.bonuses.keys():
            bomberman.bonuses.update(
                {"rollerSkate": [self, 10000, pygame.time.get_ticks()]}
            )
        if "slowDown" in bomberman.bonuses.keys():
            bomberman.bonuses.pop("slowDown")

    def cancelBonus(self, bomberman):
        bomberman.vel = 2
        bomberman.rect.x -= bomberman.rect.x % 2
        bomberman.rect.y -= bomberman.rect.y % 2


class InvincibilityPowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.isInvincible = True
        bomberman.bonuses.update(
            {"invincibility": [self, 15000, pygame.time.get_ticks()]}
        )

    def cancelBonus(self, bomberman):
        bomberman.isInvincible = False


class GhostPowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.ghost = True
        bomberman.bonuses.update({"ghost": [self, 15000, pygame.time.get_ticks()]})

    def cancelBonus(self, bomberman):
        if not bomberman.level.tiles[bomberman.i][bomberman.j].isFreeToStepOff():
            bomberman.die()
        bomberman.ghost = False


class ObstaclePowerUp(PowerUp):
    def __init__(self, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def applyBonus(self, bomberman):
        bomberman.obstaclesNum += 3


# CURSES:


class SlowDownCurse(Curse):
    def __init__(self, i, j, x, y):
        super().__init__(x, y, i, j)

    def applyBonus(self, bomberman):
        bomberman.vel = 1
        if "slowDown" not in bomberman.bonuses.keys():
            bomberman.bonuses.update(
                {"slowDown": [self, 10000, pygame.time.get_ticks()]}
            )
        if "rollerSkate" in bomberman.bonuses.keys():
            bomberman.bonuses.pop("rollerSkate")

    def cancelBonus(self, bomberman):
        bomberman.vel = 2
        bomberman.rect.x -= bomberman.rect.x % 2
        bomberman.rect.y -= bomberman.rect.y % 2


class ShortRangeCurse(
    Curse
):  # The blast range of the bombs placed by the player should be only 1 field for a certain time
    def __init__(self, i, j, x, y):
        super().__init__(x, y, i, j)

    def applyBonus(self, bomberman):
        bomberman.blastRange = 2
        bomberman.bonuses.update({"shortRange": [self, 15000, pygame.time.get_ticks()]})

    def cancelBonus(self, bomberman):
        bomberman.blastRange = 3


class NoBombsCurse(Curse):
    def __init__(self, i, j, x, y):
        super().__init__(x, y, i, j)

    def applyBonus(
        self, bomberman
    ):  # overriding applyBonus function of the Bonus superclass
        bomberman.noBombs = True
        bomberman.bonuses.update({"noBombs": [self, 12000, pygame.time.get_ticks()]})

    def cancelBonus(self, bomberman):
        bomberman.noBombs = False


class ImmediatePlacingCurse(Curse):

    def __init__(self, i, j, x, y):
        super().__init__(x, y, i, j)

    def applyBonus(self, bomberman):
        bomberman.immediateBombs = True
        bomberman.bonuses.update(
            {"immediatePlacing": [self, 8000, pygame.time.get_ticks()]}
        )

    def cancelBonus(self, bomberman):
        bomberman.immediateBombs = False
