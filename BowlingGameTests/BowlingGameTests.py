import unittest

class BowlingGameTests(unittest.TestCase):

    def testAllZeroRollsScoresZero(self):
        game = Game()
        self.assertEqual(0, game.score())
def main():
        unittest.main()

if __name__ == '__main__':
    main()