import random


def bet(chips, player_input):
    global chips_bet
    chips_bet = player_input
    chips -= int(chips_bet)
    print(f"You now have {chips} chips")
    return chips

def showcards(player_cards, player_value, dealer_cards, dealer_value):
    print(f"Your cards are: {player_cards}")
    print(f"Your total value is: {player_value}\n")
    
    print(f"Dealers cards are: {dealer_cards}")
    print(f"Dealer total value is: {dealer_value}\n")

# def dealcards(x,personcards,personvalue, cards):
#         for i in range(0,x):
#             random_key, random_value = random.choice(list(cards.items()))
#             personcards.append(random_key)
#             personvalue += random_value

def playerlose():
    pass