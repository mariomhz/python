# rock, paper, scissors
import random
def main():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("invalid input, try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"computer chose: {computer_choice}")
        if user_choice == computer_choice: print("it's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
        play_again = input("Do you want to play again? [Yes/No] ").lower()
        if play_again != "yes": print("exiting game...") 
        break
if __name__ == "__main__":
    main()
            
            
        
        