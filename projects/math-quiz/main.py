import random
import time

number_of_questions = 5
operators = ["+", "-", "*"]

print("welcome to math quiz game.".upper())
start = time.time()
while number_of_questions > 0:
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    # c = random.randint(0, len(operators)-1)
    c = random.choice(operators)

    main_answer  = 0 

    if c == "+":
        main_answer = a + b
    elif c == "-":
        main_answer = a - b
    elif c == "*":
        main_answer = a * b


    while main_answer != int(input(f"{a} {c} {b} = ")):
        pass


    number_of_questions -= 1

else:
    end = time.time()

print("your record is:", round(end - start, 2))
    
                          