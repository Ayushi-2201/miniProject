import random

import time

OPERATORS = ["+", "-", "*"]
MAX_VALUE = 12
MIN_VALUE = 3
TOTAL_QUESTIONS = 10

continue_game = "y"

def question_generator():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATORS)

    question = (str(left) + " " + operator + " " + str(right))
    answer = eval(question)
    return question, answer

while True:
    if continue_game == "n":
        break
    else:
        wrong = 0
        input("Press enter to start! ")
        print("--------------------------------------------\n\n")

        start_time = time.time()

        for i in range (TOTAL_QUESTIONS):

            question, answer = question_generator()
            
            while True:
                
                guess = input("Problem #" + str(i+1) + "  : " + question + " = ")

                if answer == int(guess):
                    break
                elif answer is str:
                    print("Enter a numeric answer!")
                else:
                    print("Wrong answer!")
                    wrong += 1
        end_time = time.time()

        print("\n\n")
        print("--------------------------------------------\n\n")

        total_time = round(end_time - start_time, 0)

        print("Nice work! You answered all questions correctly in", total_time, "seconds.")
        if wrong == 1:
            print("You took a total of", wrong, " retry to answer all questions.\n\n")
        elif wrong == 0 :
            pass
        else :
            print("You took a total of", wrong, " retries to answer all questions.\n\n")

        continue_game = input("Do you want to continue playing (y/n): ").lower()
        print("\n\n")
    
