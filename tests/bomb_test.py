import unittest


class TestBomb(unittest.TestCase):
    """
    Sample test for CI
    """

    def test_pass(self):
        self.assertFalse(3 > 4)


if __name__ == "__main__":
    unittest.main()
