def deg_cal():

    print("Welcome to Python Degree Calculator!")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print(f"The temperature in Celsius is: {celsius:.2f}°C")
    print("Thanks Habibi for using this calculator!")

deg_cal()