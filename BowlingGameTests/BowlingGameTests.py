import unittest

from BowlingGame import Game


class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def rollManyBalls(self, ballsToRoll, pinsHit):
        for i in range(0, ballsToRoll):
            self.game.roll(pinsHit)

    def rollASpare(self):
        self.game.roll(6)
        self.game.roll(4)

    def rollAStrike(self):
        self.game.roll(10)

    def testAllZeroRollsScoresZero(self):
        self.rollManyBalls(20, 0)
        self.assertEqual(0, self.game.score())

    def testAllOneRollsScoresTwenty(self):
        self.rollManyBalls(20, 1)
        self.assertEquals(20, self.game.score())

    def testGameWithASpare(self):
        self.rollASpare()
        self.game.roll(3)
        self.rollManyBalls(17, 0)
        self.assertEquals(16, self.game.score())

    def testGameWithAStrike(self):
        self.rollAStrike()
        self.game.roll(3)
        self.game.roll(2)
        self.rollManyBalls(16, 0)
        self.assertEqual(20, self.game.score())

    def testPerfectGame(self):
        self.rollManyBalls(12, 10)
        self.assertEqual(300, self.game.score())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
