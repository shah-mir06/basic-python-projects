import time

def countdown_python(seconds):

    '''
    A simple Python Countdown that ask to user for specific amount of time and then Start a CountDown in Seconds
    '''
    while seconds > 0:
        minutes, remaining_seconds = divmod(seconds, 3600)  
        display_time = "{:02d}:{:02d}".format(minutes, remaining_seconds)
        print(display_time, end="\r")
        time.sleep(1)
        seconds = seconds - 1
    print("Timer Completed!")
print("Python Countdown Timer")
user_time = input("How many seconds to countdown? : ")
print("\nThank You for Using!!")


if __name__ == "__main__":

    countdown_python(int(user_time))
