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


def test_return_solved_result_if_matched_number(game):
    game.question = '123'
    assert_matched_number(game.guess("123"), True, 3, 0)


def test_return_solved_result_if_unmatched_number(game):
    game.question = '123'
    assert_matched_number(game.guess("456"), False, 0, 0)
