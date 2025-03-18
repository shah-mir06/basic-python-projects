import random

def hangman_game_python():

    '''
    A simple Python Hangman Game that Ask to user to Try Guess the word form the Given list in Three Attepmts Which Computer has A random Choice Guess.
    ["python", "computer", "programming", "hangman", "developer"]

    '''

    word_list = ["python", "computer", "programming", "hangman", "developer"]
    secret_word = random.choice(word_list)

    word_progress = ["_"] * len(secret_word) 
    lives = 6
    guessed_letters = []

    print("Welcome to Python Hangman Game!")
    print("Try to guess the word, one letter at a time.")

    while lives > 0 and "_" in word_progress:
        print("Word:", " ".join(word_progress))
        print(f"Attempts left: {lives}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good job! That letter is in the word.")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[index] = guess
        else:
            print("Wrong guess!")
            lives -= 1


    if "_" not in word_progress:
        print("Congrats! You guessed the word:", secret_word)
    else:
        print("Game Over! The correct word was:", secret_word)


        print("\nThank you for playing!")

if __name__ == "__main__":

    hangman_game_python()

