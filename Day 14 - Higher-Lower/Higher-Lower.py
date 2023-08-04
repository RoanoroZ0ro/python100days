from game_data import data
import random
from art import logo, vs
import sys

def get_data():
    selected_data = random.choice(data)
    name = selected_data["name"]
    description = selected_data["description"]
    country = selected_data["country"]

    print(f"{name}, a {description}, from {country}")
    return selected_data


def compare(a, b, score):
    choice = input("Who has more followers? Type 'A' or 'B':")
    if choice == 'A':
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}.")
            return score, a
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return sys.exit()
    elif choice == 'B':
        if b["follower_count"] > a["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}.")
            return score, b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return sys.exit()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return sys.exit()


def game():
    score = 0
    print(logo)

    a = get_data()
    print(vs)
    b = get_data()

    score, a = compare(a, b, score)

    name = a["name"]
    description = a["description"]
    country = a["country"]

    print(f"{name}, a {description}, from {country}")
    print(vs)
    b = get_data()

    while score:
        score, a = compare(a, b, score)

        name = a["name"]
        description = a["description"]
        country = a["country"]

        print(f"{name}, a {description}, from {country}")
        print(vs)
        b = get_data()

    return score


print(game())
