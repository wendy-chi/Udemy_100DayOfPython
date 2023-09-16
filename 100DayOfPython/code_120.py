import random


def compare(u_num, com_num):
    if u_num == com_num:
        print(f"You got it. The number is {u_num}")
        return 1
    elif u_num < com_num:
        print("too low")
        return 0
    else:
        print("too high")
        return 0


def guess(attempts):
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_number = int(input("Make a guess:"))
        if compare(user_number, computer_number) == 0:
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
            else:
                print("Guess again.")
        else:
            attempts = -1


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

computer_number = random.randint(1, 100)
#print(f"computer_number: {computer_number}")

remain_attempts = 0

if difficulty == 'hard':
    remain_attempts = 5
    guess(remain_attempts)
else:
    remain_attempts = 10
    guess(remain_attempts)


