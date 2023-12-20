import pytest
from functions_under_test import deal_cards, bet

def test_deal_cards_value():
    personcards = []
    personvalue = 0
    x = 2
    personvalue = deal_cards(personcards, personvalue, x)
    # Expected result is a integer at a value of 2 or above to pass
    assert personvalue >= 2

def test_deal_cards_cards():
    personcards = []
    personvalue = 0
    x = 2
    personvalue = deal_cards(personcards, personvalue, x)
    # Expected result is a fail as the len of cards should be 2
    assert len(personcards) == 3

def test_bet():
    player_input = 30
    chips = 100
    chips, chips_bet = bet(player_input, chips)
    # Expected result is pass as player input and chips bet value should be the same and input should be taken from chips value
    assert chips == 70 and chips_bet == 30