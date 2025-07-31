class Game:
    ...

    def guess(self, guess_number):
        self._assert_illegal_value(guess_number)

    def _assert_illegal_value(self, guess_number):
        if len(guess_number) != 3:
            raise TypeError('Input length must be 3')

        if not guess_number.isdigit():
            raise TypeError('Non-number mixed')

        if set(guess_number) != 3:
            raise TypeError('Duplicated number exists')


class GameResult:
    ...