import random
class NegativeBet(Exception):
    pass
cards = {
    "Ace11" : 11,
    "Ace1" : 1,
    "King" : 10,
    "Queen" : 10,
    "Jack" : 10,
    "Ten" : 10,
    "Nine" : 9,
    "Eight" : 8,
    "Seven" : 7,
    "Six" : 6,
    "Five" : 5,
    "Four" : 4,
    "Three" : 3,
    "Two" : 2
    }

def deal_cards(personcards, personvalue, x):
    for i in range(0,x):
        random_key, random_value = random.choice(list(cards.items()))
        personcards.append(random_key)
        personvalue += random_value
    return personvalue

def bet(player_input,chips):
    while True:
        try:
            if player_input == "exit":
                exit()
            chips_bet = int(player_input)
            if chips_bet < 0:
                raise NegativeBet("Cant bet negative chips!")
            elif chips_bet > chips:
                raise ValueError("Cant bet chips ya dont have!")
            chips -= chips_bet
            return chips, chips_bet
        except ValueError:
            print("Thats not a valid input!")
            player_input = input("Please try Again! ")
        except NegativeBet as e:
            print(e)
            player_input = input("Please try Again! ")


