# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


theNumber = random.randint(1, 100)

print(f"Pssst, the correct answer is {theNumber}")

gameLevel = input("Choose a difficulty. Type 'easy' or 'hard':")


times = 5
if gameLevel == "easy":
    times = 10

print(f"You have {times} attempts remaining to guess the number.")

while times >= 1:
    guess = int(input("Make a guess:"))
    if guess == theNumber:
        print(f"You got it! The answer was {guess}.")
        break
    else:
        print("Too low." if guess<theNumber else "Too high.")
        times = times-1
        if times == 0:
            print("You've run out of guesses, you lose.")
        else:
            print(f"You have {times} attempts remaining to guess the number.")