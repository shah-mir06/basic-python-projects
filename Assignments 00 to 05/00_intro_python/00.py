def add():
    print("Welcome to Python Sum Calculator.")
    
    userinput1 = input("Enter Your First Number Please: ")
    userinput2 = input("Enter Your Second Number Please: ")

    try:
        total = int(userinput1) + int(userinput2)  
        print(f"The sum of both numbers is: {total}")
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

    print("Thanks Habibi for using this calculator!")

add()

