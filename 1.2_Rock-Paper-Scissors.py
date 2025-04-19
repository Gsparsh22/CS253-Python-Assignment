import random
import numpy as np

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors', 'quit']
    while True:
        user_input = input("Enter your choice (Rock, Paper, Scissors or Quit): ").strip().lower() # taking in users input and turning it into lower case so it becomes case insensitive
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please enter Rock, Paper, Scissors, or Quit.") # if the input is not from the choices povided and is some invalid input

def get_computer_choice():
    return np.random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'    # tie in case of same choice
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'    # win conditions
    else:
        return 'loss' # if does not wins and ties, then losses

def main():
    wins = 0
    losses = 0
    ties = 0

    print("Welcome to Rock-Paper-Scissors") # first intro to the RPS game
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Thanks for playing") # greeting on exiting the game
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        if result == 'win':
            print("You win this round")
            wins += 1
        elif result == 'loss':
            print("You lose this round")
            losses += 1
        else:
            print("It's a tie")
            ties += 1

        print(f"Score -> Wins: {wins}, Losses: {losses}, Ties: {ties}\n") # score tally after each round

if __name__ == "__main__":
    main()