import random

print("Welcome to guessing number game.")


while True:
    want_to_play = input("\nAre you ready to play? (y/n) ")
    if want_to_play == "n":
        print("Bye...")
        break

    elif want_to_play == "y":

        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        n = int(input("Enter the number of chances: "))
        number = random.randint(start, end)

        while n >= 1:
            a = int(input("pick a number: "))

            n = n - 1

            if a == number:
                print("congradulation, you won the game ;)")
                break

            if n == 0:
                continue

            if a > number:
                print(f"your number is too high, you only have #{n} chances.")
            else:
                print(f"your number is too small, you only have #{n} chances.")

        else:
            print("Maybe it's not your day ;(")
            print(f"The actuall number is: {number}")
    else:
        print("Please enter a valid input")
