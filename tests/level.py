import unittest
from unittest.mock import Mock
from level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.level = Level([], self.screen, {})

    def test_initial_setup(self):
        # Ensure that all required attributes are initialized correctly
        self.assertIsNotNone(self.level.tiles)
        self.assertIsNotNone(self.level.bombermans)
        self.assertIsNotNone(self.level.monsters)


if __name__ == "__main__":
    unittest.main()
