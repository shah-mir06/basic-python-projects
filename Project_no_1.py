def mad_lib():
    """
    A simple Mad Libs game that generates a short story based on user input.
    """

    print("\nWelcome to the Python Mad Libs Story!")
    print("Answer the questions below to generate your personalized story.\n")

    name = input("Enter your name: ").strip()
    occupation = input("Enter your occupation: ").strip()
    field_of_study = input("What do you study? ").strip()

    if not name or not occupation or not field_of_study:
        print("\nError: All fields are required. Please try again.\n")
        return
 
    print("\nYour Story:")
    print(f"My name is {name}, and I am a {occupation}. I study {field_of_study} with great dedication.")
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    mad_lib()
