# Blackjack Terminal App Overview
The aim of the this application is exhibit my skills as a python programmer by implementing different features in the app and to use a wide range of developer tools to assist in consutruction and implementation of the app.

# Code Style Guide
The coding style I abided by was Pep8 as it was the most similiar styling convention to what was used in class. When doing research into pep8 I had came across a rescource known as flake8 which points out code pep8 errors within the code and specifies the line. Initialing I was overwhelemed with the errors as there were so many:

## Errors
```
main.py:16:12: E203 whitespace before ':'
main.py:17:11: E203 whitespace before ':'
main.py:18:11: E203 whitespace before ':'
main.py:19:12: E203 whitespace before ':'
main.py:20:11: E203 whitespace before ':'
main.py:21:10: E203 whitespace before ':'
main.py:22:11: E203 whitespace before ':'
main.py:23:12: E203 whitespace before ':'
main.py:24:12: E203 whitespace before ':'
main.py:25:10: E203 whitespace before ':'
main.py:26:11: E203 whitespace before ':'
main.py:27:11: E203 whitespace before ':'
main.py:28:12: E203 whitespace before ':'
main.py:29:10: E203 whitespace before ':'
main.py:32:1: E302 expected 2 blank lines, found 0
main.py:35:1: E302 expected 2 blank lines, found 0
main.py:38:1: E302 expected 2 blank lines, found 0
main.py:41:1: W293 blank line contains whitespace
main.py:45:1: E302 expected 2 blank lines, found 0
main.py:53:1: E302 expected 2 blank lines, found 0
main.py:54:21: E231 missing whitespace after ','
main.py:60:1: E302 expected 2 blank lines, found 0
main.py:60:21: E231 missing whitespace after ','
main.py:79:1: E302 expected 2 blank lines, found 0
main.py:82:52: W291 trailing whitespace
main.py:84:1: E302 expected 2 blank lines, found 0
main.py:85:80: E501 line too long (106 > 79 characters)
main.py:91:1: W293 blank line contains whitespace
main.py:101:26: W291 trailing whitespace
main.py:106:1: E302 expected 2 blank lines, found 0
main.py:112:1: E305 expected 2 blank lines after class or function definition, found 1
main.py:113:80: E501 line too long (361 > 79 characters)
main.py:126:19: E712 comparison to True should be 'if cond is True:' or 'if cond:'
main.py:129:44: E231 missing whitespace after ','
main.py:134:1: W293 blank line contains whitespace
main.py:137:80: E501 line too long (95 > 79 characters)
main.py:149:13: E303 too many blank lines (2)
main.py:158:1: W293 blank line contains whitespace
main.py:161:1: W293 blank line contains whitespace
main.py:163:69: W291 trailing whitespace
main.py:166:1: W293 blank line contains whitespace
main.py:167:41: W291 trailing whitespace
main.py:178:1: W293 blank line contains whitespace
main.py:180:80: E501 line too long (85 > 79 characters)
main.py:184:80: E501 line too long (91 > 79 characters)
main.py:189:1: W293 blank line contains whitespace
main.py:201:12: W292 no newline at end of file
```

When looking through these errors I noticed I had made alot of mistakes but alot of theses mistakes happened continusly through my code and the variety of the errors was quite low. The first main error was 203, this error showed up 14 lines in a row and pointed to my dictionary variable called cards. The varaible did not abide by the pep8 guidelines as I had a space before and after the ":" seperating the *true value pairs*.

---
#### Before:
```python
    "Ace11" : 11,
```

#### After:
```python
    "Ace11": 11,
```
---
E302 was the next constant appearing error and was to do with lacking blank lines between declared functions and classes. The change noticably increased readability of the code

---
#### Before:
```python
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

```

#### After:
```python
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
```
---
The errors w293 and w291 are both erros thats point to random whitespace either on blank lines(w93) or trailing whitespace afer written code(w91). Initially when fixing up white space errors I wondered what the point of it was. It didnt seem to hurt the readability of the code at all or really do anything. After doing some googling I definitely wasnt the only one who was confused, but a few *possible* answers came of the search. The main answer I liked was found on a forum about how it messes with text editors and compared it to how if your focusing on something and then someone inturupts you it messes with your focus. A few other answers included messing the compilers causing them to skip lines and programs taking up more space as the whitepace is considered a character.

e501 is an error code that points to lines of code that are too long. The main reason why long code is a bad thing is alot of people code with a preview up or a code checker on the other half of their screen. If code is too long it makes this a bit more difficult. Personally I had used a few longer lines of code the biggest grievance against this guidline was on the prompt variable on line 132 now or 113 back then coming in at a whopping 361 characters, four and a half times the reccommeneded 79 characters per line.

---

#### Before:
```python
rules = "Your aim is to be closer to the number 21 but not over it with the dealt cards than the dealer. As the player you have the option to [bold]'hit'[/bold], to gain an extra card, [bold]'stand'[/bold] to keep ur value as is and end the round, [bold]'surrender'[/bold], to gain back half of the betted chips and lose the round. The value of the cards are: "
```

#### After:
```python
rules = ("Your aim is to be closer to the number 21,"
        "but not over it with the dealt cards than the dealer."
        "As the player you have the option to [bold]'hit'[/bold],"
        "to gain an extra card, [bold]'stand'[/bold] to keep your value as is"
        "and end the round, [bold]'surrender'[/bold],"
        "to gain back half of the betted chips and lose the round."
        "The value of the cards are: ")
```
E712 focused on the wording used in an if true statement. The specific example initially had the the equality idenitifer (==) and was checking if the variable 'round start' was equal to true. Pep8 doesnt like this and preferes the 'is' comparison singleton. This way of avoids potential issues in regards to object ident.ity

---

#### Before:
```python
if roundstart == True:
```
#### After:
```python
if roundstart is True:
```
---

E231 is an error regarding me missing a space after a comma. Usually I do this automatically but there are points in which I do miss it occasionally. This does highlight the use of programs such as flake8 that act like a code proof reader to find things that you miss.

E303 is flagged is I leave too many blank lines between statements of code. Keeping a consistent number of lines improves the readability of code immensely.

W292 much like its brother W291 and W293 confused me on why it reccommonded by the pep8 styling guide. After some quick searching I had found out that within the UNIX and Linux ecosystem it expects text files to end in a newline. This convetion is still used today and the reason why pep8 reccomends it.




## Naming
The general naming convention used throughout the code is in-line with the pep8 style guide. In the guide it says for functions and variable names to use lowercase with words being seperated with underscores. The only time when this can be broken is when declaring constants; variables that cannot be changed. The convention used when declaring constants is uppercase with words being seperatated with underscores. When naming classes the style guide says to use CamelCase.

---
#### Variable
```python
chips_bet = 0
```
#### Function
```python
def reset_round():
```
#### Constant
```python
BLACKJACK = 21
```
#### Class
```python
class SurrenderError(Exception):
```
---

## Summary of pep8
Overall pep8 can be *mostly* followed when coding naturally and without thinking too hard about it. But when fixing up code to match the style guide perfectly as well as looking over the style guide. Pep8 can be incredibly finicky and unintuative when it comes to more advanced stuff. For instance the pep8 style guide prefers tab to not be used and instead indentation should be done manually with spaces. Which I am sure serves some purpose, personally it just seems unintuitive. Going forward for different projects I will do research into different styling guides to find one that makes more sense to me.

# Features

The App has many different features that allow users to interact with the app within the terminal window.
## Main Game loop
Within the main game loop the app has 4 main features. In the loop the user will be prompted with different options about how they should go about progressing. Within the loop the user is able to exit the game at any time by inputing the 'exit' into the prompt. If a user inputs a invalid input such as a number or a word that isnt recognised it will bring an up and error message asking for the user to try again. 

### Bet
At the begining of hand the user is shown how many chips they currently have and asks them to bet an amount of chips on them wining the hand. If users try to bet negative chips a custom error is raised, if they try to be more chips then they currently have or enter a invalid input a value error is raised. A when loop is utilised so that users can try again after an error has been raised. The feature itself is mostly contained within the bet function.

#### Function:
```python
# Function to determine the value of the chips and chips_bet variables
def bet(player_input, chips):
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
```
#### Custom Error Class:
```python
# Error class made to catch negative bets
class NegativeBet(Exception):
    pass
```

### Hit
This feature will most likely be the most used. It allows the user to make the decision to 'hit' this 'deals' the player an extra card to increase their value. The feature uses the CARDS variable as its source and uses a loop to simulate cards being dealt as they would in a usual deck.The feature itself is containted within the deal_cards function and is used to deal the initial two cards for the player and the dealer as well as being used for the hit feature. This feature can be used when the player is asked to 'hit', 'stand' or 'surrender', and can be called upon when typing 'hit' into the prompt

```python
# Function to deal cards to player or dealer
def deal_cards(personcards, personvalue, x):
    for i in range(0, x):
        random_key, random_value = random.choice(list(CARDS.items()))
        personcards.append(random_key)
        personvalue += random_value
    return personvalue
```

### Stand
The 'stand' feature allows the user the user to sit on their value and cards, but also prohibits them making any further actions within the hand. This feature gives the user an extra layer of strategy when playing, as they can decide to sit on some values and hope the dealer cant beat it and bust rather then just hit and bust themselves. This feature can be used when the player is asked to 'hit', 'stand' or 'surrender', and can be called upon when typing 'stand' into the prompt.

### Surrender
The 'surrender' feature allows user to surrender on the first action of a hand. This feature is used when users believe they have been dealt an incrdibly bad hand or the dealer an incredibly good hand. It allows users to purposly 'lose' the round to get half of their betted chips back. If user trys to surrender on rounds apart from the first  it will check for how many cards in hand and raise a custom error if the user has more then 2 cards.

#### Surrender block:
```python
        elif player_input == "surrender":
            # Try block to catch surrender input after initial round
            try:
                if len(player_cards) == 2:
                    chips += chips_bet/2
                    print("You have surrendered!")
                    print(f"You now have {chips} chips")
                    player_lose()
                else:
                    raise SurrenderError

            except SurrenderError:
                print("You can only surrender on the first round of a hand!")
```
#### Custom Error Class:
```python
# Error class made for the surrender 'elif' block
class SurrenderError(Exception):
    pass
```