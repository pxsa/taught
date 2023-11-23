import time
# import os

while True:
    a = input("Are you ready to start the timer? (y/n): ")
    if a == "n":
        print("Thanks, bye ;)")
        break

    elif a == "y":
        h = int(input("enter the hour: "))
        m = int(input("enter the minute: "))
        s = int(input("enter the second: "))

        total = h * 3600 + m * 60 + s

        while total >= 0:
            # os.system("clear")
            print(total, "\r", end="")
            time.sleep(1)
            total = total - 1