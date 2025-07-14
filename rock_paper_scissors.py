import random

options = {"r":"rock","p":"paper", "s":"scissors"}
   
user_score = 0
computer_score = 0

choices = list(options.values())

print("let's play Rock, Paper, Scissors!")
print("Type 'r' for rock, 'p' for paper, or 's' for scissors.\n")

while True:
    user_input = input("Enter your choice (rock, paper or scissors): ").lower()

    if user_input not in options:
        print("Invalid input\nPlease type r, p, or s.\n")
        continue

    user_choice = options[user_input]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!!")
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
        (user_choice == 'paper' and computer_choice == 'rock') or 
        (user_choice == 'scissors' and computer_choice == 'paper')):
        print("congratulations!!\nYou won!")
        user_score += 1
    else:
        print("you lost\nComputer won this round.")
        computer_score += 1

    print(f"Score: You = {user_score} and Computer = {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        print(f"Final Score: You = {user_score} and Computer = {computer_score}")
        break
