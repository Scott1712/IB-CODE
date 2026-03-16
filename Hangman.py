#Scott De'Ath
#15/01/25
import random

solo = True

def clear():
    print("\n" * 100)
def one():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
def two():
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
def three():
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
def four():
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
def five():
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
def six():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
def seven():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
def hide(array,guess):
    for i in array:
        print(i,end=" ")
    print("\n" * 2)
    print("Guesses -> ",end=" ")
    for i in guess:
        print(i,end=" ")
    print("\n" * 2)
soloWords = ['baboon','koala','rawr']

if solo == True:
    message = soloWords[random.randint(0,len(soloWords))-1]
else:
    lower = False
    while lower == False:
        message = str(input("Enter the code: "))
        lower = True
        for char in message:
            if (ord(char) < 97 or ord(char) > 122) and ord(char) != 32:
                lower = False
                print("*Only lowercase/spaces please*")
                print("")

wrong = 0
win = False
word = []
hidden = []
guesses = []

for char in message:
    word.append(char)
for char in message:
    if ord(char) == 32:
        hidden.append(" ")
    else:
        hidden.append("_")

while wrong == 0 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    one()
    hide(hidden,guesses)
    while goodGuess == False:
        enter = str(input("Guess -> "))
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
while wrong == 1 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    two()
    hide(hidden,guesses)
    while goodGuess == False:
        enter = str(input("Guess -> "))
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
while wrong == 2 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    three()
    hide(hidden,guesses)
    while goodGuess == False:
        enter = str(input("Guess -> "))
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
while wrong == 3 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    four()
    hide(hidden,guesses)
    while goodGuess == False:
        enter = str(input("Guess -> "))
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
while wrong == 4 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    five()
    hide(hidden,guesses)
    while goodGuess == False:
        enter = str(input("Guess -> "))
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
while wrong == 5 and win == False:
    win = True
    goodGuess = False
    correct = False
    clear()
    six()
    hide(hidden,guesses)
    while goodGuess == False:
        if enter == message:
            win = True
            goodGuess = True
        else:
            if len(enter)!=1:
                print("*1 Lowercase please*")
            else:
                if ord(enter)>122 or ord(enter)<97:
                    print("*1 Lowercase please*")
                else:
                    goodGuess = True
                    for i in range(0,len(word)):
                        if enter == word[i]:
                            hidden[i]=enter
                            correct = True
                    if correct == False:
                        wrong +=1
                        guesses.append(enter)
            for i in range(0,len(word)):
                if word[i]!=hidden[i]:
                    win = False
clear()
if wrong == 0:
    one()
if wrong == 1:
    two()
if wrong == 2:
    three()
if wrong == 3:
    four()
if wrong == 4:
    five()
if wrong == 5:
    six()
if wrong == 6:
    seven()
hide(word,guesses)
if win == True:
    print("Yay! You won!")
if win == False:
    print("Sorry... you lost.")