import unittest
from unittest.mock import Mock
import pygame
from gameSprite import GameSprite, Transparency


class TestGameSprite(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface((50, 50))
        self.sprite = GameSprite(100, 150, 0, 1, self.image)

    def test_initial_position(self):
        self.assertEqual(self.sprite.rect.x, 100)
        self.assertEqual(self.sprite.rect.y, 150)

    def test_absorbExplosion(self):
        # As the method is empty, we are just testing it does not raise an error
        try:
            self.sprite.absorbExplosion()
        except Exception as e:
            self.fail(f"absorbExplosion raised an exception {e}")

    def test_transparency_inheritance(self):
        transparent = Transparency(200, 250, 2, 3, self.image)
        self.assertIsInstance(transparent, GameSprite)


if __name__ == "__main__":
    unittest.main()
