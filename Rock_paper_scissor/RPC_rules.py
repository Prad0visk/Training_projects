#defining function and rules.

#header menu
def show_header():
    print("="*40)
    print(f'Welcome✊ 🖐️ ✌️ '.center(38))
    print("="*40)
    print(f'Let\'s play rock, paper and scissors!:')
    print("="*40)

def get_player_choice():
    while True:
        try:
            choice = int(input("""1) Rock
            2) Paper
            3) Scissor
            Choose one to play: """.strip()))
        except ValueError:
            print("Invalid input!")
            continue
        if choice <1 or choice >3:
            print("insert only 1,2 or 3!")
            continue

        return choice

#"translate" player input so it can be easier to use in rules.
def get_choice_name(choice)
    if choice == 1:
        return "rock"
    elif choice ==2:
        return "paper"
    elif choice == 3:
        return "scissor"

#the rules of the game.
def game_rules(computer_choice,player_choice):
    if computer_choice == player_choice:
        return "tie"
    elif computer_choice == "rock" and player_choice =="scissor":
        return "computer"
    elif computer_choice =="paper" and player_choice =="rock":
        return "computer"
    elif computer_choice == "scissor" and player_choice =="paper":
        return "computer"
    else:
        return "player"

def game_menu():


