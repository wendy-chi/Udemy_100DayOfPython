from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    select_card = choice(cards)
    return select_card


def calculate_score(input_list):
    score = sum(input_list)
    if input_list == [10, 11] or input_list == [11, 10]:
        print("a blackjack in our game")  # Ace + 10
        return 0
    if score > 21 and 11 in input_list:
        input_list.remove(11)
        input_list.append(1)
    return score


def compare(final_user_score, final_computer_score):
    if final_user_score > 21 and final_computer_score > 21:
        print("You went over. You lose 😤")
    if final_user_score == final_computer_score:
        print("Draw 🙃")
    elif final_computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif final_user_score == 0:
        print("Win with a Blackjack 😎")
    elif final_user_score > 21:
        print("You went over. You lose 😭")
    elif final_computer_score > 21:
        print("Opponent went over. You win 😁")
    elif final_user_score > final_computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")


def new_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"user_cards: {user_cards}")
    print(f"computer_first_card:{computer_cards[0]}")

    continue_add_card = True
    while continue_add_card:
        user_score = calculate_score(user_cards)
        com_score = calculate_score(computer_cards)

        print(f"user score: {user_score}")
        if user_score == 0 or com_score == 0 or user_score > 21:
            continue_add_card = False
            #new_game()
        else:
            selection = input("Do you want to get another card?")
            if selection == "y":
                another_card = deal_card()
                user_cards.append(another_card)
                user_score = calculate_score(user_cards)
                print(user_cards)
            else:
                continue_add_card = False
        while com_score != 0 and com_score < 17:
            computer_cards.append(deal_card())
            com_score = calculate_score(computer_cards)
            continue_add_card = False
        print(f"computer_cards: {computer_cards}")
        compare(user_score, com_score)
        continue_add_card = False


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    new_game()
