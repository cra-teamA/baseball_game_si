class Game:
    def __init__(self):
        self._question = '123'
    @property
    def question(self):
        raise AttributeError('읽을 수 없는 속성')

    @question.setter
    def question(self, question):
        self._question = question

    def guess(self, guess_number):
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        return GameResult(False, 0, 0)

    def _assert_illegal_value(self, guess_number):
        if len(guess_number) != 3:
            raise TypeError('Input length must be 3')

        if not guess_number.isdigit():
            raise TypeError('Non-number mixed')

        if len(set(guess_number)) != 3:
            raise TypeError('Duplicated number exists')


class GameResult:
    def __init__(self, solved, strikes, balls):
        self. _solved = solved
        self. _strikes = strikes
        self. _balls = balls
    @property
    def solved(self):
        return self._solved
    @property
    def strikes(self):
        return self._strikes
    @property
    def balls(self):
        return self._balls