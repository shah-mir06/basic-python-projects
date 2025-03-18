import random 

def computer_guesses_number():  
    
    """
    A simple Secret Number Game that Computer Guess a Secret Number of  User.
    """

    print("Think of a number between 1 and 100.")  
    low = 1  
    high = 100  

    while True:
        guess = (low + high) // 2  
       
        feedback = input(f"Is your number {guess}? (Enter 'higher', 'lower', or 'correct'): ").lower() 

        if feedback == 'higher':  
            low = guess + 1  
        elif feedback == 'lower':  
            high = guess - 1  
        elif feedback == 'correct':  
            print("Great! The computer guessed your number.")  
            break
        else:  
            print("Please enter 'higher', 'lower', or 'correct'.")  

        print("\nThank you for playing!")

if __name__ == "__main__":

    computer_guesses_number()
