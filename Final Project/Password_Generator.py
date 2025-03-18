import random

def password_generator():
    
    '''
    A simple Python Password generator That Generate the Passwords on Users Demands.
    '''
    print("Welcome to Python Password Generator")
    characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?._"
    number=int(input("How Many Passwords Do Wanna Generate?:"))
    lenght=int(input("Enter the lenght of the Password:"))
    print("Here is your Confidentional Password, Don't share it with anyone!")
    for password in range (number):
        passwords = ""
        for p in range (lenght):
            passwords += random.choice(characters)
        print(passwords)
    print("Thank you for Using Python Password Generator.")

if __name__ == "__main__":

    password_generator()


