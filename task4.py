import random

def game():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Rules: Rock beats Scissors, Paper beats Rock, Scissors beats Paper\n")

    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter your choice (rock/paper/scissors or q to quit): ").lower()
        if user == "q":
            print("Thanks for playing! Goodbye 👋")
            break
        if user not in choices:
            print("Invalid choice! Try again.")
            continue

        comp = random.choice(choices)
        print(f"Computer chose: {comp}")

        if user == comp:
            print("It's a Tie!!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You Win! 🎉")
        else:
            print("Computer Wins!!")
        print("-" * 40)

game()
