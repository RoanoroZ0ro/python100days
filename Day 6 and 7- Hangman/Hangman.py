import random
#from replit import clear #it works on replit, not in pycharm
#import os
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
lives = 6


print(logo)
#testing:
print(f'Psst, the solution is {chosen_word}')

display = []
for letter in chosen_word:
    display += "_"

print(display)


while "_" in display:
    guess = input("Try to guess a letter: ")

    #clear()
    #os.system('cls')

    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        lives -= 1
    print(display)
    print(stages[lives])
    if lives == 0:
        break

if lives != 0:
    print("You have won!")
else:
    print("You have lost! :(")