import pytest

from game import Game, GameResult


@pytest.fixture()
def game():
    return Game()


def assert_illegal_input(game, inputs):
    with pytest.raises(TypeError):
        game.guess(inputs)

@pytest.mark.parametrize("invalid_input", [None, "12", "1245", "12d", "121"])
def test_exception_when_invalid_inputs(game, invalid_input):
    assert_illegal_input(game, invalid_input)


def test_return_solved_result_if_matched_number(game):
    result:GameResult = game.guess("123")
    assert result is None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0

