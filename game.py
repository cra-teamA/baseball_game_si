class Game:
    ...

    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        try:
            guessNumber = int(guessNumber)
        except ValueError:
            raise TypeError()