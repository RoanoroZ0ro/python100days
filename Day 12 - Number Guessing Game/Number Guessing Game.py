from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def make_a_guess():
    number = int(input("Make a guess: "))
    return number


def select_difficulty():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == 'easy':
        turns = EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        turns = HARD_LEVEL_TURNS
    else:
        print("Wrong input. You will be playing hard")
        turns = HARD_LEVEL_TURNS
    return turns


def play_game():
    print(logo)

    answer = random.randint(1, 100)
    print(f'Pssst, answer is: {answer} :)')

    turns = select_difficulty()

    while turns > 0:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = make_a_guess()
        if guess == answer:
            print(f'You got it! The answer was {answer}.')
            return
        else:
            if answer > guess:
                print("Too low.")
            else:
                print("Too high.")
            turns -= 1

        if turns == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Try again.")


play_game()
