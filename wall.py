from gameSprite import GameSprite


class Wall(GameSprite):
    """
    A class to represent the wall object
    """

    def __init__(self, level, i, j, x, y, image):
        super().__init__(x, y, i, j, image)

    def absorbExplosion(self):
        """
        Walls are immune to explosions
        :return:
        """
        pass
