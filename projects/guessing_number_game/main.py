import random

print("welcome to Gussing Number Game.".upper())

a = int(input("Enter the number of chances: "))
number = random.randint(1, 10)

while a > 0:
    guess = int(input("guess number: "))
    a = a -1

    if guess == number:
        print("Congradulation, What a super choice.")
        break

    if a == 0: 
        print("Maybe it's not your day...")

    elif guess < number:
        print(f"your number is too smaller, you have only {a} chances.")
    else:
        print(f"your number is too larger, you have only {a} chances.")
