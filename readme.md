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