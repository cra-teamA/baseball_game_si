import pytest

from game import Game


@pytest.fixture()
def game():
    return Game()


def assert_illegal_input(game, inputs):
    with pytest.raises(TypeError):
        game.guess(inputs)

@pytest.mark.parametrize("invalid_input", [None, "12", "1245", "12d", "121"])
def test_exception_when_invalid_inputs(game, invalid_input):
    assert_illegal_input(game, invalid_input)



