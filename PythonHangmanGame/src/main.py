import random

word_list = ["python", "hangman", "challenge"]

secret_word = random.choice(word_list)

correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

def display_game_state():
    displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"word: {displayed_word}")
    print(f"incorrect guesses: {' '.join(incorrect_guesses)}")
    print(f"attempts left: {attempts_left}")
    
while True:
    display_game_state()
    guess = input("enter your guess: ").lower()
    
    if guess in secret_word:
        correct_guesses.add(guess)
        if set(secret_word).issubset(correct_guesses):
            print(f"Congrats! you've guessed the word! it was '{secret_word}'!")
            break
    else:
        incorrect_guesses.add(guess)
        attempts_left -= 1
        if attempts_left == 0:
            print("GAME OVER!")
            print(f"the secret word was: {secret_word}")
            break