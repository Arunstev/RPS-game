import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("enter your choice(rock,paper,scissors):")
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors, you win:)"
        else:
            return "Paper cover rock, younlose:("
    elif player == "paper":
        if computer == "rock":
            return "paper cover the rock, you win:)"
        else:
            return "scissor cuts the paper, you lose:("
    elif player == "scissors":
        if computer == "paper":
            return "scissor cuts the paper, you win:)"
        else:
            return "rock smashes scissors, you lose:("
        
choices = get_choices()
result =check_win(choices['player'],choices['computer'])
print(result)
        