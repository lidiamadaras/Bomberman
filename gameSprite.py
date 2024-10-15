import pygame


class GameSprite(pygame.sprite.Sprite):
    """
    Base class to represent a sprite object, extends pygame.sprite.Sprite with image and indexes on the map
    attributes and the absorbExplosion() function
    """

    def __init__(self, x, y, i, j, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.i = i
        self.j = j

    def absorbExplosion(self):
        pass


class Transparency(GameSprite):
    """
    A class to represent the battle royale feature's preview of the incoming wall
    """

    def __init__(self, x, y, i, j, image):
        super().__init__(x, y, i, j, image)
