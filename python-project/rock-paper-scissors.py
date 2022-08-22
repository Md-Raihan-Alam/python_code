import random
data=["rock","paper","scissors"]
def choices():
    player=input("\nEnter rock,paper,scissors:")
    if player!="rock" and player!="paper" and player!="scissors":
        print("\nGame cancel. Invalid Input")
        {"player":"player","computer":0}
    else:
        computer=random.choice(data)
    return {"player":player,"computer":computer}

def game_result(data):
    player_choice=data["player"]
    computer_choice=data["computer"]
    if player_choice=="player":
        return "\nGame Terminated!!!!!"
    else:
        print(f"\nPlayer choose {player_choice} and Bot choose {computer_choice}")
    if player_choice==computer_choice:
        return "\nIt's a tie!!!!"
    elif player_choice=="rock" and computer_choice=="paper":
        return "\nPaper catch rock. Bot wins"
    elif player_choice=="rock" and computer_choice=="scissors":
        return "\nRock smash scissors. Player wins"
    elif player_choice=="paper" and computer_choice=="rock":
        return "\nPaper catch rock. Player wins"
    elif player_choice=="paper" and computer_choice=="scissors":
        return "\nScissors cut paper. Bot wins"
    elif player_choice=="scissors" and computer_choice=="rock":
        return "\nRock smash scissors. Bot wins"
    elif player_choice=="scissors" and computer_choice=="paper":
        return "\nScissors cut paper. Player wins"

print("\nWelcome to rock-paper-scissors-game made by python. Programmer Raihan")
data_list=choices()
result=game_result(data_list)
print(result)