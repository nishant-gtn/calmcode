from blackjack.common import card_score


# def test_simple_usecase1():
#     assert card_score("JK") == 20


# def test_simple_usecase2():
#     assert card_score("JKQ") == 0


# def test_simple_usecase3():
#     assert card_score("KA") == 21


# def test_simple_usecase4():
#     assert card_score("AA") == 12


import pytest


@pytest.mark.parametrize(
    "cards,score", [("JK", 20), ("KKK", 0), ("AA", 12), ("AK", 21)]
)
def test_simple_usecase(cards, score):
    assert card_score(cards) == score


def test_value_error_is_raised1():
    with pytest.raises(ValueError):
        card_score("")


def test_value_error_is_raised2():
    with pytest.raises(ValueError):
        card_score(1)
