import random

def secret_game_num():
    """
    A Secret Number Game that Guess a Secret Number of computer.
    """
    secret_number:int=random.randint(1,200)
    guess=0

    print("Hey There! Welcome to Python Guessing Number Game (1-50).")
    print("Let's start this!!!")


    while secret_number != guess:
        guess=int(input("Take You guess:"))
        if guess < secret_number:
            print("Please try again,it's too low!!")
        elif guess > secret_number:
            print("Please try again it's too high!!")
        else:
            print(f"Congratulations!! you Have guessed the secret number {guess} Correctly.")

        print("\nThank you for playing!")

if __name__ == "__main__":
    
    secret_game_num()