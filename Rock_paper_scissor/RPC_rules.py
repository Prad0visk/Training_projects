import random

def show_header():
    print("="*40)
    print(f'Welcome✊ 🖐️ ✌️ '.center(38))
    print("="*40)
    print(f'Let\'s play rock, paper and scissors!:')
    print("="*40)

def get_choice_name(choice)
    if choice == 1:
        return "rock"
    elif choice ==2:
        return "paper"
    elif choice == 3:
        return "scissor"

def game_rules(computer_choice,player_choice):
    if computer_choice == player_choice:
        return "tie"
    elif computer_choice == "rock" and player_choice =="scissor":
        return "computer"
    elif computer_choice =="paper" and player_choice =="rock":
        return "computer"
    elif computer_choice == "scissors" and player_choice =="paper":
        return "computer"
    else:
        return "player"



