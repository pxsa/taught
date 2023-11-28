import random

random_number = random.randint(1, 10)
chances = 5

while chances > 0:
    user_number = int(input("Enter a number(1/10): "))

    chances -= 1

    if user_number == random_number:
        print("you win the game.")
        break

    if chances == 0:
        print(f"sorry, you lose the game. the actual number was {random_number}")

    elif user_number < random_number:
        print(f"your number is too small. you only have {chances} chances.")

    elif user_number > random_number:
        print(f"your number is too large. you only have {chances} chances.")