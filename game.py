class Game:
    ...

    def guess(self, guessNumber):
        self._assert_illegal_value(guessNumber)

    def _assert_illegal_value(self, guessNumber):
        if len(guessNumber) != 3:
            raise TypeError('Input length must be 3')
        try:
            _ = int(guessNumber)
        except ValueError:
            raise TypeError('Non-number mixed')

        if list(guessNumber) != set(list(guessNumber)):
            raise TypeError('Duplicated number exists')
