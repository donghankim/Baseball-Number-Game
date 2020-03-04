# Baseball-Number-Game
Recreated a popular text based game played in Korea (숫자야구 게임)

## Motivation
This project helped me understand the dynamics of creating a basic GUI application in python. Used the built-in library tkinter.

## Rules of the Game
This is a two player game that is very popular in South Korea. Each player sets a four digit number at the start of the game. The objective of the game is to guess the opponents number. 

Each player takes turns guessing what their opponents number is. After every guess, the opponent (in this case, the computer) tells you have many "strikes" and how many "balls" you manage to hit. Stike represent the case when the number you guess is in the same place as the opponents number. Ball represents the case when the number you guess is within the opponents number, but not in the right place. For example, if the opponents number is 1234, and you guess 1203, then the opponent will inform you that you managed to get 2 strikes (from the 1 and 2) and one ball (from the 3). The game ends when either player gets their opponents number.

When setting numbers, you cant have a number with recurring (repeating) digits, and the length of the digit must be 4. 

## Installation
Make sure you have python3 installed on your device. The tkiner library comes as default for all versions of python. Therefore, there is no need to install any additional packages.

## Run
To run the game, type in this command in your terminal (or cmd if on windows):
```python
python3 baseball_main.py
```

Three windows will open, the first two windows will be for the players to enter their number. The third window is a simple GUI that tells you how many strikes and balls each player has managed to achieve. The game will not start until both players have entered their respective number. 
