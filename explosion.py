import pygame
from gameSprite import GameSprite

tile_size = 48


class Explosion(GameSprite):
    """
    A class to represent a piece of an explosion occupying one tile
    """

    def __init__(self, id, x, y, i, j, image):
        super().__init__(
            x,
            y,
            i,
            j,
            pygame.transform.scale(image, (0.875 * tile_size, 0.875 * tile_size)),
        )
        self.id = id
        self.initTime = pygame.time.get_ticks()

    def affect(self, sprite):
        """
        Causes the sprite that collides with the explosion react to it
        :param sprite:
        :return:
        """
        if pygame.sprite.collide_rect(self, sprite):
            sprite.absorbExplosion()
