import pytest

from game import Game, GameResult


@pytest.fixture()
def game():
    return Game()


def assert_illegal_input(game, inputs):
    with pytest.raises(TypeError):
        game.guess(inputs)


def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls


@pytest.mark.parametrize("invalid_input", [None, "12", "1245", "12d", "121"])
def test_exception_when_invalid_inputs(game, invalid_input):
    assert_illegal_input(game, invalid_input)


@pytest.mark.parametrize(
    'question,guess_number,solved,strikes,balls',
    [
        ('123', '123', True, 3, 0),
        ('123', '456', False, 0, 0),
        ('123', '124', False, 2, 0),
        ('123', '321', False, 1, 2)
    ]
)
def test_return_solved_result(game, question, guess_number, solved, strikes, balls):
    game.question = question
    assert_matched_number(game.guess(guess_number), solved, strikes, balls)

