# Tried to make a Guessing a Number Game

import random

print("Hello There , Enter your Name")
name = input()
print("Welcome", name)
print("Hey,", name, "I am Thinking of a Number Between 1 and 30")
secretNumber = random.randint(1, 30)

for guesses in range(6):
    print("Take a Guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is Lower than the Number")
    elif guess > secretNumber:
        print("Your Guess in Higher than the Number")
    else:
        break

if guess == secretNumber:
    print("Woah,", name, "You Guessed it Right,", "You Guessed it in", guesses, "times")

else:
    print("No the Right Number was ", str(secretNumber))
