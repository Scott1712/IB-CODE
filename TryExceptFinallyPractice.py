#25/08/2025

import random

levels = 0
special = random.randint(1,10)

while True:
    try:
        guess = input("Guess a number 1-10 ->   ").strip()
        if int(guess) < 1 or int(guess) > 10:
            raise ValueError("Outside of range")
        else:
            if int(guess) == special:
                print("Oh no, you guessed it")
                break
            levels += 1
            print("You are safe ("+str(levels)+" times)")
    except ValueError as e:
        print("Re-enter a value")
    finally:
        print("")

print("Good game")