# Blackjack Terminal App Overview
The aim of the this application is exhibit my skills as a python programmer by implementing different features in the app and to use a wide range of developer tools to assist in construction and implementation of the app.

# Code Style Guide
The coding style I abided by was Pep8 as it was the most similar styling convention to what was used in class. When doing research into pep8 I had came across a resource known as flake8 which points out code pep8 errors within the code and specifies the line. Initialing I was overwhelmed with the errors as there were so many:

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

When looking through these errors I noticed I had made a lot of mistakes but a lot of theses mistakes happened continuously through my code and the variety of the errors was quite low. The first main error was 203, this error showed up 14 lines in a row and pointed to my dictionary variable called cards. The variable did not abide by the pep8 guidelines as I had a space before and after the ":" separating the *true value pairs*.

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
E302 was the next constant appearing error and was to do with lacking blank lines between declared functions and classes. The change noticeably increased readability of the code

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
The errors w293 and w291 are both errors thats point to random whitespace either on blank lines(w93) or trailing whitespace after written code(w91). Initially when fixing up white space errors I wondered what the point of it was. It didn't seem to hurt the readability of the code at all or really do anything. After doing some googling I definitely wasn't the only one who was confused, but a few *possible* answers came of the search. The main answer I liked was found on a forum about how it messes with text editors and compared it to how if your focusing on something and then someone interrupts you it messes with your focus. A few other answers included messing the compilers causing them to skip lines and programs taking up more space as the whitespace is considered a character.

e501 is an error code that points to lines of code that are too long. The main reason why long code is a bad thing is a lot of people code with a preview up or a code checker on the other half of their screen. If code is too long it makes this a bit more difficult. Personally I had used a few longer lines of code the biggest grievance against this guideline was on the prompt variable on line 132 now or 113 back then coming in at a whopping 361 characters, four and a half times the recommended 79 characters per line.

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
E712 focused on the wording used in an 'if true' statement. The specific error initially had the the equality identifier (==) and was checking if the variable 'round start' was equal to true. Pep8 doesn't like this and prefers the 'is' comparison singleton. This way avoids potential issues in regards to object identity.

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

E231 is an error regarding missing a space after a comma. Usually I do this automatically but there are points in which I do miss it occasionally. This does highlight the use of programs such as flake8 that act like a code proof reader to find things that you miss.

E303 is flagged if I leave too many blank lines between statements of code. Keeping a consistent number of lines improves the readability of code immensely.

W292 much like its brother W291 and W293 confused me on why it recommended by the pep8 styling guide. After some quick searching I had found out that within  UNIX and Linux ecosystems it expects text files to end in a newline. This convention is still used today and the reason why pep8 recommended it.




## Naming
The general naming convention used throughout the code is in-line with the pep8 style guide. In the guide it says for functions and variable names to use lowercase with words being separated with underscores. The only time when this can be broken is when declaring constants; variables that cannot be changed. The convention used when declaring constants is uppercase with words being separated with underscores. When naming classes the style guide says to use CamelCase.

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
Overall pep8 can be *mostly* followed when coding naturally and without thinking too hard about it. But when fixing up code to match the style guide perfectly as well as looking over the style guide. Pep8 can be incredibly finicky and unintuitive when it comes to more advanced stuff. For instance the pep8 style guide prefers tab to not be used and instead indentation should be done manually with spaces. Which I am sure serves some purpose, personally it just seems unintuitive. Going forward for different projects I will do research into different styling guides to find one that makes more sense to me.

# Features

The App has many different features that allow users to interact with the app within the terminal window.
## Main Game loop
Within the main game loop the app has 4 main features. In the loop the user will be prompted with different options about how they should go about progressing. Within the loop the user is able to exit the game at any time by inputing the word 'exit' into the prompt. If a user inputs a invalid input such as a number or a word that isn't recognized it will bring an up and error message asking for the user to try again. 

### Bet
At the beginning of the hand the user is shown how many chips they currently have and asks them to bet an amount of chips on them wining the hand. If users try to bet negative chips a custom error is raised, if they try to be more chips then they currently have or enter a invalid input a value error is raised. A when loop is utilized so that users can try again after an error has been raised. The feature itself is mostly contained within the bet function.

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
This feature will most likely be the most used. It allows the user to make the decision to 'hit' this 'deals' the player an extra card to increase their value. The feature uses the CARDS variable as its source and uses a loop to simulate cards being dealt as they would in a usual deck.The feature itself is contained within the deal_cards function and is used to deal the initial two cards for the player and the dealer as well as being used for the hit feature. This feature can be used when the player is asked to 'hit', 'stand' or 'surrender', and can be called upon when typing 'hit' into the prompt

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
The 'surrender' feature allows user to surrender on the first action of a hand. This feature is used when users believe they have been dealt an incredibly bad hand or the dealer an incredibly good hand. It allows users to purposely 'lose' the round to get half of their betted chips back. If user tries to surrender on rounds apart from the first  it will check for how many cards in hand and raise a custom error if the user has more then 2 cards.

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
## Dealer Logic Feature
When playing blackjack at a casino you are against the dealer and the dealer has to abide by a strict set of rules for their decision making so that the casino can have the highest profit margin as possible. I wanted to emulate this to a degree to get. Whenever a player makes a decision the 'dealer' will run through a bunch of 'if' statements to determine its next move. With using normal casino dealer rules it allowed me to get a basic idea on how to go about coding it. The basic logic the dealer runs by is that if its value is less then 16 or lower then the players value it will 'hit' and gain an extra card. If the dealer value is greater 16 the dealer will keep its value waiting for another action by the player. Adding a feature like this and personifying it creates a way more engaging and exciting experience for the user and gives a lot of replayability.

## Minor Features

- Player name being recorded
- Dynamic and changing chip count based on player win or lose
- color coded UI for easier readability
- The ability to exit at anytime once in the main game loop
- The use of 'emojis' to add character and flavour
- Try and except blocks throughout the code to catch invalid inputs       
 
# Help Documentation

## How to play Blackjack
Blackjack is a casino game where your aim is to be closer to the number 21, blackjack, as the dealer. As the player you have 2-3 option each round in a hand. To hit, to gain an extra card and add that cards value to your total value. To stand, to sit on your current value and forfeit the ability to make any further moves in the current hand. Surrender is only available during the first round of a hand and is used to purposely lose in order to gain back half of your betted chip.

## Steps To Install
The src code comes with 3 separate bash files 2 for depending on you operating system and a third that named 'make_exe.sh' that creates an exe located in the folder dist that the bash file creates. For the other bash files; Open VS code in the directory where they are located type in 'sh run_blackjack_windows.sh' or 'sh run_blackjack_mac.sh' depending on your OS and the bash script will run and install all the needed packages from the 'requirements.txt' file and will run within the terminal on vscode.


## Commands
As specified before the entire game is played through the command line using keyboard input for words that are prompted by the app. The main commands are:

- Hit for main game loop
- Stand for main game loop  
- Surrender for main game loop
- y for play again input
- n for play again input
- exit to quit the app
- name input
- bet input

## System Requirements
- 1.6GHz or faster processor
- 1GB Ram

## Dependencies
- emoji package
- rich package
- random package

# Project Management
When looking for resources to do project management a lot of websites used a Kanban layout. Personally I found Kanban layout a bit hard to read. I found a website called 'height' that allowed for 4 separate views; Spreadsheet, Kanban, Calender and Gantt. 'height also allows me to export the project as seen as a csv and allows me to give other people access to the project. The CSV import and some associated screenshots are the main way I decided to prove use of project management being used through out the creation of the app.
### Screenshots

![image](./project%20managment%20proof/pythoncodedone%20img.PNG)
![image](./project%20managment%20proof/readmestart%20img.PNG)
![image](./project%20managment%20proof/readme%20nearly%20done%20mimg.PNG)
![image](./project%20managment%20proof/project%20management%20done.PNG)


### CSV
#### Day 0
```
"Tasks","Status","Assignees","Lists"
"20 Commits to Repo","To do","","#terminal-app-blackjack"
"Project Flowchart","To do","","#terminal-app-blackjack"
"Start the Chart","To do","","#terminal-app-blackjack"
"Finish the Chart","To do","","#terminal-app-blackjack"
"Python Code","To do","","#terminal-app-blackjack"
"Other Criteria","To do","","#terminal-app-blackjack"
"Uses Loops and Conditional Control","To do","","#terminal-app-blackjack"
"Variables and Values global and local scope","To do","","#terminal-app-blackjack"
"Functions Written ","To do","","#terminal-app-blackjack"
"Betting Function","To do","","#terminal-app-blackjack"
"Stand Function","To do","","#terminal-app-blackjack"
"Hit Function","To do","","#terminal-app-blackjack"
"Surrender Function","To do","","#terminal-app-blackjack"
"Bug Testing","To do","","#terminal-app-blackjack"
"Test Case 1","To do","","#terminal-app-blackjack"
"Test Case 2","To do","","#terminal-app-blackjack"
"Test Play","To do","","#terminal-app-blackjack"
"DRY Principle","To do","","#terminal-app-blackjack"
"Script That Makes Progam a exe","To do","","#terminal-app-blackjack"
"Python Package/s","To do","","#terminal-app-blackjack"
"Package 1","To do","","#terminal-app-blackjack"
"Package 2","To do","","#terminal-app-blackjack"
"Package 3","To do","","#terminal-app-blackjack"
"Package 4","To do","","#terminal-app-blackjack"
"Readme Documentaion","To do","","#terminal-app-blackjack"
"Outline and describe Features Present","To do","","#terminal-app-blackjack"
"Show Proof of use of Project Planner","To do","","#terminal-app-blackjack"
"Referenced Sources","To do","","#terminal-app-blackjack"
"Link to Repo","To do","","#terminal-app-blackjack"
"Identify style guide or styling conventions","To do","","#terminal-app-blackjack"
"Help Documention","To do","","#terminal-app-blackjack"
"Presentation","To do","","#terminal-app-blackjack"
"Features Listed","To do","","#terminal-app-blackjack"
"Walkthrough of logic","To do","","#terminal-app-blackjack"
"General Progress documented","To do","","#terminal-app-blackjack"
"Favourite Parts","To do","","#terminal-app-blackjack"
"Difficult Parts","To do","","#terminal-app-blackjack"
"Gameplay Loop Recorded","To do","","#terminal-app-blackjack"
```
#### Week 1
```
"Tasks","Status","Assignees","Lists"
"Python Code","To do","","#terminal-app-blackjack"
"Functions Written ","To do","","#terminal-app-blackjack"
"Function4","To do","","#terminal-app-blackjack"
"Function5","To do","","#terminal-app-blackjack"
"Function6+","To do","","#terminal-app-blackjack"
"Bug Testing","To do","","#terminal-app-blackjack"
"Test Case 1","To do","","#terminal-app-blackjack"
"Test Case 2","To do","","#terminal-app-blackjack"
"Test Play","To do","","#terminal-app-blackjack"
"DRY Principle","In progress","","#terminal-app-blackjack"
"Script That Makes Progam a exe","To do","","#terminal-app-blackjack"
"Python Package/s","To do","","#terminal-app-blackjack"
"Package 2","To do","","#terminal-app-blackjack"
"Package 3","To do","","#terminal-app-blackjack"
"Package 4","To do","","#terminal-app-blackjack"
"Readme Documentaion","To do","","#terminal-app-blackjack"
"Outline and describe Features Present","To do","","#terminal-app-blackjack"
"Show Proof of use of Project Planner","To do","","#terminal-app-blackjack"
"Referenced Sources","To do","","#terminal-app-blackjack"
"Link to Repo","To do","","#terminal-app-blackjack"
"Identify style guide or styling conventions","To do","","#terminal-app-blackjack"
"Help Documention","To do","","#terminal-app-blackjack"
"Presentation","To do","","#terminal-app-blackjack"
"Features Listed","To do","","#terminal-app-blackjack"
"Walkthrough of logic","To do","","#terminal-app-blackjack"
"General Progress documented","To do","","#terminal-app-blackjack"
"Favourite Parts","To do","","#terminal-app-blackjack"
"Difficult Parts","To do","","#terminal-app-blackjack"
"Gameplay Loop Recorded","To do","","#terminal-app-blackjack"
"20 Commits to Repo","To do","","#terminal-app-blackjack"
```

#### Python Code Done
```
"Tasks","Status","Assignees","Lists"
"Readme Documentaion","To do","","#terminal-app-blackjack"
"Outline and describe Features Present","To do","","#terminal-app-blackjack"
"Show Proof of use of Project Planner","To do","","#terminal-app-blackjack"
"Referenced Sources","To do","","#terminal-app-blackjack"
"Link to Repo","To do","","#terminal-app-blackjack"
"Identify style guide or styling conventions","To do","","#terminal-app-blackjack"
"Help Documention","To do","","#terminal-app-blackjack"
"Presentation","To do","","#terminal-app-blackjack"
"Features Listed","To do","","#terminal-app-blackjack"
"Walkthrough of logic","To do","","#terminal-app-blackjack"
"General Progress documented","To do","","#terminal-app-blackjack"
"Favourite Parts","To do","","#terminal-app-blackjack"
"Difficult Parts","To do","","#terminal-app-blackjack"
"Gameplay Loop Recorded","To do","","#terminal-app-blackjack"
"20 Commits to Repo","To do","","#terminal-app-blackjack"
"16-20 Commits","To do","","#terminal-app-blackjack"
"20+ Commits","To do","","#terminal-app-blackjack"
"Extra Stuff","To do","","#terminal-app-blackjack"
"Create leaderboard using .csv file","To do","","#terminal-app-blackjack"
```

#### Readme Start
```
"Tasks","Status","Assignees","Lists"
"Readme Documentaion","To do","","#terminal-app-blackjack"
"Outline and describe Features Present","To do","","#terminal-app-blackjack"
"Show Proof of use of Project Planner","To do","","#terminal-app-blackjack"
"Referenced Sources","To do","","#terminal-app-blackjack"
"Link to Repo","To do","","#terminal-app-blackjack"
"Help Documention","To do","","#terminal-app-blackjack"
"Presentation","To do","","#terminal-app-blackjack"
"Features Listed","To do","","#terminal-app-blackjack"
"Walkthrough of logic","To do","","#terminal-app-blackjack"
"General Progress documented","To do","","#terminal-app-blackjack"
"Favourite Parts","To do","","#terminal-app-blackjack"
"Difficult Parts","To do","","#terminal-app-blackjack"
"Gameplay Loop Recorded","To do","","#terminal-app-blackjack"
"20 Commits to Repo","To do","","#terminal-app-blackjack"
"Extra Stuff","To do","","#terminal-app-blackjack"
"Create leaderboard using .csv file","To do","","#terminal-app-blackjack"
```

#### Readme Nearly Done
```
"Tasks","Status","Assignees","Lists"
"Python Code","Done","","#terminal-app-blackjack"
"Other Criteria","Done","","#terminal-app-blackjack"
"Functions Written ","Done","","#terminal-app-blackjack"
"Function2","Done","","#terminal-app-blackjack"
"Function3","Done","","#terminal-app-blackjack"
"Function4","Done","","#terminal-app-blackjack"
"Function5","Done","","#terminal-app-blackjack"
"Function6+","Done","","#terminal-app-blackjack"
"Bug Testing","Done","","#terminal-app-blackjack"
"Handles All Possible Errors","Done","","#terminal-app-blackjack"
"Test Case 1","Done","","#terminal-app-blackjack"
"Test Case 2","Done","","#terminal-app-blackjack"
"Test Play","Done","","#terminal-app-blackjack"
"DRY Principle","Done","","#terminal-app-blackjack"
"Script That Makes Progam a exe","Done","","#terminal-app-blackjack"
"Python Package/s","Done","","#terminal-app-blackjack"
"Package 1","Done","","#terminal-app-blackjack"
"Package 2","Done","","#terminal-app-blackjack"
"Package 3","Done","","#terminal-app-blackjack"
"Package 4","Done","","#terminal-app-blackjack"
"Readme Documentaion","To do","","#terminal-app-blackjack"
"Outline and describe Features Present","Done","","#terminal-app-blackjack"
"Show Proof of use of Project Planner","To do","","#terminal-app-blackjack"
"Referenced Sources","To do","","#terminal-app-blackjack"
"Link to Repo","To do","","#terminal-app-blackjack"
"Identify style guide or styling conventions","Done","","#terminal-app-blackjack"
"Help Documention","Done","","#terminal-app-blackjack"
"Presentation","To do","","#terminal-app-blackjack"
"Features Listed","To do","","#terminal-app-blackjack"
"Walkthrough of logic","To do","","#terminal-app-blackjack"
"General Progress documented","To do","","#terminal-app-blackjack"
"Favourite Parts","To do","","#terminal-app-blackjack"
"Gameplay Loop Recorded","To do","","#terminal-app-blackjack"
"20 Commits to Repo","Done","","#terminal-app-blackjack"
"5-10 Commits","Done","","#terminal-app-blackjack"
"11-15 Commits","Done","","#terminal-app-blackjack"
"16-20 Commits","Done","","#terminal-app-blackjack"
"20+ Commits","Done","","#terminal-app-blackjack"
"Extra Stuff","To do","","#terminal-app-blackjack"
"Create leaderboard using .csv file","To do","","#terminal-app-blackjack"
```

#### Readme Done
```
"Tasks","Status","Assignees","Lists"
"Extra Stuff","To do","","#terminal-app-blackjack"
"Create leaderboard using .csv file","To do","","#terminal-app-blackjack"
```
## Flowchart
![image](./project%20managment%20proof/Blackjack%20Flowchart.png)

# Links
### Repository
- https://github.com/DefineTal/T1A3-Terminal_Application

### Project Management Link
- https://height.app/rxNC-k-ciG/terminal-app-blackjack

### Presentation
- https://youtu.be/Ggvge8iYvNI

# References
- PEP 8 – Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/