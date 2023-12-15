from blackjack_functions import bet
import random

chips = 100
player_value = 0
player_cards = []
dealer_value = 0
dealer_cards = ""
blackjack = 21
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
prompt = "Please enter your name: "
rules = "Your aim is to be closer to the number 21 with the dealt cards then the dealer. As the player you have the option to 'hit', to gain an extra card, 'stand' to keep ur value as is and end the round, 'surrender', to gain back half of the betted chips and lose the round. The value of the cards are: "

print(prompt)
player_name = str(input())
print(f"Hello {player_name}! Welcome to the Blackjack Casino!")
print(rules, cards)

input("Press 'Enter' to continue! ")
player_input = ""
while player_input != "exit":
    print(f"You have {chips} chips")
    player_input = input("How much would you like to bet? ")
    chips = bet(chips, player_input)

    for i in range(0,2):
        random_key, random_value = random.choice(list(cards.items()))
        player_cards.append(random_key)
        player_value += random_value
 
    print(f"Your cards are: {player_cards}")
    print(f"Your total value is: {player_value}\n")

    print(f"Dealers Cards are: ")

    