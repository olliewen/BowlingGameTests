class Game():
    def __init__(self):
        self.rolls = [0] * 21
        self.rollIndex = 0

    def roll(self, pins):
        self.rolls[self.rollIndex] = pins
        self.rollIndex += 1

    def score(self):
        score = 0
        frameStartIndex = 0
        for frame in range(0, 10):
            if self.isStrike(frameStartIndex):  # Strike
                score += 10 + self.strikeBonus(frameStartIndex)
                frameStartIndex += 1
            elif self.isSpare(frameStartIndex):
                score += 10 + self.spareBonus(frameStartIndex)
                frameStartIndex += 2
            else:
                score += self.sumOfBallsInFrame(frameStartIndex)
                frameStartIndex += 2
        return score

    def strikeBonus(self, frameStartIndex):
        return self.rolls[frameStartIndex + 1] + self.rolls[frameStartIndex + 2]

    def spareBonus(self, frameStartIndex):
        return self.rolls[frameStartIndex + 2]

    def sumOfBallsInFrame(self, frameStartIndex):
        return self.rolls[frameStartIndex] + self.rolls[frameStartIndex + 1]

    def isSpare(self, frameStartIndex):
        return (self.rolls[frameStartIndex] + self.rolls[frameStartIndex + 1]) == 10

    def isStrike(self, frameStartIndex):
        return self.rolls[frameStartIndex] == 10
