import random

def rock_paper_scissor():
    
    """
    A simple Rock, Paper & Scissor Game that Play's the Game With User.
    """
    print("Hey There, Welcome to Python Rock Paper & Scissor Game.")

    choices=["rock","paper","scissor"]

    print("Let's have some Fun!")
        
    player=input("Enter Your Choice (Rock or Paper or Scissor): ").lower()

    if player not in choices:
            print("Invalid Choice.Please Enter the Correct Choice.")
            return
    computer=random.choice(choices)
    if computer == player:
            print("It's Tie, try Again Please.")

    elif player =="rock" and computer == "scissor":
            print("Congratulations! you Win.")

    elif player == "scissor" and computer == "papar":
            print("Congratulations! you Win.")
    
    elif player == "paper" and computer == "rock":
            print("Congratulations! You Win.")

    else:
            print("You Lose! Computer Win.")

    print("Thanks for Playing Have a Nice Day.")


    print("\nThank you for playing!")

if __name__ == "__main__":

        rock_paper_scissor()