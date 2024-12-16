import random
words = ["python", "hangman", "programming", "developer", "code", "csharp", "powershell", "wicked", "playstation"]

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to the hangman game!")
    
    while attempts > 0:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"remaining attempts: {attempts}")
        
        guess = input("enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("enter a single letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Nice! {guess} is in word!")
        else: 
            attempts -= 1
            print(f"Oops! {guess} is not in the list!")
            
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! you guessed the word: {word}!")
            break
    if attempts == 0:
        print(f"\nGAME OVER! The word was '{word}'")
if __name__ == "__main__":
    main()