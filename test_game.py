import pytest

from game import Game


@pytest.fixture()
def game():
    return Game()


def assert_illegal_input(game, inputs):
    try:
        game.guess(inputs)
        pytest.fail()
    except TypeError:
        pass


def test_exception_when_invalid_inputs(game):
    assert_illegal_input(game, None)
    assert_illegal_input(game, "12")
    assert_illegal_input(game, "1245")
    assert_illegal_input(game, "12d")


