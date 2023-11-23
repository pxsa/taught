import random

print("welcome to Gussing Number Game.".upper())

a = int(input("Enter the number of chances: "))
# number = random.randint(1, 10)
number = int(input("Enter a number: "))

start = 1
end = 100

while a > 0:
    # guess = int(input("guess number: "))
    guess = random.randint(start, end)
    a = a -1

    if guess == number:
        print(f"Your Choose {guess}, Congradulation, What a super choice.")
        break

    elif guess < number:
        print(f"your number, {guess} is too smaller, you have only {a} chances.")
        start = guess+1
    else:
        print(f"your number, {guess} is too larger,  you have only {a} chances.")
        end = guess-1
else:
    print("Maybe it's not your day...")
