import random

def bet(chips, player_input):
    chips_bet = int(player_input)
    chips -= chips_bet
    print(f"You now have {chips} chips")
    return chips



