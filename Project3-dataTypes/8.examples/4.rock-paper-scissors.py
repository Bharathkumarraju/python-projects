import random

def get_computer_choice():
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    random_number = random.randint(1,3)
    computer_choice =  options[random_number]

    return computer_choice

def get_user_input():
    while True:
        user_input = input("Enter rock/paper/scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid input! Please enter only rock, paper, or scissors.")


def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return "draw"
    # condition for user to win
    elif user_pick == "paper" and computer_pick == "rock":
        return "win"
    elif user_pick == "rock" and computer_pick == "scissors":
        return "win"
    elif user_pick == "scissors" and computer_pick == "paper":
        return "win"
    # all other conditions result to loss
    else:
        return "lose"

if __name__ == '__main__':
     users_input = get_user_input()
     print(f"Your pick: {users_input}")
     machine_choice = get_computer_choice()
     print(f"Computer's pick: {machine_choice}")
     result = get_result(users_input,machine_choice)
     print(f"You {result}")





