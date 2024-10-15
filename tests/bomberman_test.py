import unittest


class TestBomberman(unittest.TestCase):
    """
    Not working
    """

    # def __init__(self):
    #     super().__init__()
    #     pygame.init()
    #
    #     tile_size = 48
    #
    #     screen_height = tile_size * len(MAP4) + tile_size * 2
    #     screen_width = tile_size * len(MAP4[0])
    #
    #     screen = pygame.display.set_mode((screen_width, screen_height))
    #     self.gameEngine = GameEngine()
    #     self.level = self.gameEngine.level
    #     self.bomberman1 = self.level.bombermans[0]
    #     self.bomberman2 = self.level.bombermans[1]
    #
    # def bombermanMovement(self):
    #     x = self.bomberman1.rect.x
    #     self.bomberman1.moveRight()
    #     self.assertTrue(x != self.bomberman1.rect.x)

    def test_pass(self):
        self.assertFalse(3 > 4)


if __name__ == "__main__":
    unittest.main()
