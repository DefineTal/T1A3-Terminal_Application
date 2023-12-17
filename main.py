from blackjack_functions import showcards
import random

chips = 100
chips_bet = 0
roundstart = True
player_value = 0
player_cards = []
dealer_value = 0
dealer_cards = []
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
    if roundstart == True:
        print(f"You have {chips} chips")
        player_input = input("How much would you like to bet? ")
        chips_bet = player_input
        chips -= int(chips_bet)
        print(f"You now have {chips} chips")
        roundstart = False

        for i in range(0,2):
            random_key, random_value = random.choice(list(cards.items()))
            player_cards.append(random_key)
            player_value += random_value

        for i in range(0,2):
            random_key, random_value = random.choice(list(cards.items()))
            dealer_cards.append(random_key)
            dealer_value += random_value
    
    showcards(player_cards, player_value, dealer_cards, dealer_value)

    player_input = input("Would you like to hit or stand? ")

    if player_input.lower() == "hit":

        for i in range(0,1):
            random_key, random_value = random.choice(list(cards.items()))
            player_cards.append(random_key)
            player_value += random_value

        if player_value > 21:
            showcards(player_cards, player_value, dealer_cards, dealer_value)
            print("You lose this round! Do you wanna play again? y/n?")
            player_input = input()
            try:
                if player_input.lower() == "n":
                    print("Thanks for playing!")
                    break
                elif player_input.lower() == "y":
                    if chips <= 0:
                        print("You dont have the chips to play again!")
                        break
                    else:
                        player_cards = []
                        dealer_cards = []
                        player_value = 0
                        dealer_value = 0
                        roundstart = True
            except:
                print("Thats not a yes or no input! Try again")

        elif player_value <= 21:
            showcards(player_cards, player_value, dealer_cards, dealer_value)
            if dealer_value < 16:
                for i in range(0,1):
                    random_key, random_value = random.choice(list(cards.items()))
                    dealer_cards.append(random_key)
                    dealer_value += random_value
                if dealer_value > 21:
                    chips += chips_bet*2
                    print(f"You win!\n You now have {chips} chips!")
                    player_cards = []
                    dealer_cards = []
                    player_value = 0
                    dealer_value = 0
                    roundstart = True
    elif player_input == "stand":
            while dealer_value < 16 or dealer_value <= player_value:                
                for i in range(0,1):
                    random_key, random_value = random.choice(list(cards.items()))
                    dealer_cards.append(random_key)
                    dealer_value += random_value
                    showcards(player_cards, player_value, dealer_cards, dealer_value)
            if dealer_value > 21:                    
                    chips += chips_bet*2
                    print(f"You win!\n You now have {chips} chips!")
                    player_cards = []
                    dealer_cards = []
                    player_value = 0
                    dealer_value = 0
                    roundstart = True
            else:
                player_input = input()
                try:
                    if player_input.lower() == "n":
                        print("Thanks for playing!")
                        break
                    elif player_input.lower() == "y":
                        if chips <= 0:
                            print("You dont have the chips to play again!")
                            break
                        else:
                            player_cards = []
                            dealer_cards = []
                            player_value = 0
                            dealer_value = 0
                            roundstart = True
                except:
                    print("Thats not a yes or no input! Try again")

