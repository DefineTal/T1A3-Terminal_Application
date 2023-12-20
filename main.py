import random, csv
from rich import print
from emoji import emojize


# Initialising Variables
chips = 100
chips_bet = 0
roundstart = True
player_value = 0
player_cards = []
dealer_value = 0
dealer_cards = []
BLACKJACK = 21
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
# Error class made for the surrender 'elif' block
class SurrenderError(Exception):
    pass
# Error class made to catch negative bets
class NegativeBet(Exception):
    pass
# Function to show dealer and player value and cards
def show_cards():
    print(f"[bold orange1]Your cards are: {player_cards}")
    print(f"[bold orange1]Your total value is: {player_value}\n")
    
    print(f"[bold magenta]Dealers cards are: {dealer_cards}")
    print(f"[bold magenta]Dealer total value is: {dealer_value}\n")
# Function to reset variables after a hand is finished
def reset_round():
    global player_cards, dealer_cards, player_value, dealer_value, roundstart
    player_cards = []
    dealer_cards = []
    player_value = 0
    dealer_value = 0
    roundstart = True
# Function to deal cards to player or dealer
def deal_cards(personcards, personvalue, x):
    for i in range(0,x):
        random_key, random_value = random.choice(list(cards.items()))
        personcards.append(random_key)
        personvalue += random_value
    return personvalue
# Function to determine the value of the chips and chips_bet variables
def bet(player_input,chips):
    while True:
        try:
            if player_input == "exit":
                exit_game()
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
# Function for when player wins
def player_win():
    global chips
    chips += chips_bet*2
    print(f"You Win!\nYou now have {chips} chips!")  
# Function for when player loses
def player_lose():
    print("You lose this round!:crying_face: Do you wanna play again? [green1]y[/green1]/[red3]n[/red3]?")
    while True:
        player_input = input()
        try:
            if player_input not in ["y", "n"]:
                raise ValueError()
                
            elif player_input == "n":
                exit_game()

            elif player_input == "y":
                if chips <= 0:
                    print("You dont have the chips to play again!")
                    exit_game()
                else:
                    reset_round()
                    break 

        except ValueError:
            print("Thats not a yes or no input! Try again")
# Function when called exits the game gracefully
def exit_game():
    print("\nThanks for playing!", ":thumbs_up:")
    print("[bold]PROGRAM WILL NOW CLOSE")
    exit()

# Text intro
prompt = "Please enter your name: "
rules = "Your aim is to be closer to the number 21 but not over it with the dealt cards than the dealer. As the player you have the option to [bold]'hit'[/bold], to gain an extra card, [bold]'stand'[/bold] to keep ur value as is and end the round, [bold]'surrender'[/bold], to gain back half of the betted chips and lose the round. The value of the cards are: "

print(prompt)
# Determines player name
player_name = str(input())
print(f"Hello {player_name}! Welcome to the Blackjack Casino!")
print(rules, cards)

input("Press 'Enter' to continue! ")
player_input = ""
# Main game loop
while True:
    # if statement that is only active on hand start
    if roundstart == True:
        print(f"You have {chips} chips")
        player_input = input("How much would you like to bet? ")
        chips, chips_bet = bet(player_input,chips)
        print(f"You now have {chips} chips\n")
        roundstart = False
        player_value = deal_cards(player_cards, player_value, 2)
        dealer_value = deal_cards(dealer_cards, dealer_value, 2)
    
    show_cards()
    player_input = input("Would you like to hit, stand or surrender? ")
    # try block with exceptions to catch invalid inputs that do not match the designated inputs
    try:
        if player_input.lower() == "hit":

            player_value = deal_cards(player_cards, player_value, 1)

            if player_value > BLACKJACK:
                show_cards()
                print(f"You now have {chips} chips.")
                player_lose()


            elif player_value <= BLACKJACK:
                show_cards()
                if dealer_value < 16:
                    dealer_value = deal_cards(dealer_cards, dealer_value, 1)
                    if dealer_value > 21:
                        player_win()
                        reset_round()
                else:
                    print("The dealer stands!")
            
            else:
                print("The dealer stands!")
                
        elif player_input == "stand":
            while dealer_value < 16 or dealer_value <= player_value:                
                dealer_value = deal_cards(dealer_cards, dealer_value, 1)
                show_cards()
                
            if dealer_value > BLACKJACK:                                 
                player_win()
                reset_round()

            elif dealer_value == player_value:
                chips += chips_bet
                print("Its a draw! You get your chips")

            else:
                print(f"You now have {chips} chips.")
                player_lose()
    
        elif player_input == "surrender":
            # Try block to catch is player is tryin to surrender after initial action
            try:
                if len(player_cards) == 2:
                    chips += chips_bet/2
                    print("You have surrendered and have got half your betted chips back!")
                    print(f"You now have {chips} chips")
                    player_lose()
                else:
                    raise SurrenderError
                    
            except SurrenderError:
                print("You can only surrender on the first round of a hand!")

        elif player_input == "exit":
            break

        else:
            raise ValueError
    except ValueError:
        print("Please Enter: Hit, Stand or Surrender\n")

exit_game()