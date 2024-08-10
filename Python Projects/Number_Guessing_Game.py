import random

name = input("Please enter your name : ")
print("Welcome to the Number guessing game", name.capitalize(), " ;)")

playing = input("Do you want to play the game ? : ").upper()


while (playing == "YES"):
    choice_of_range = int(input("Please enter the range till which the game will procede to : 0 to number(range) you choose. "))

    print("You have to guess the number within 5 tries only.")

    count = 1
    if choice_of_range > 0:
        computer_guess = random.randrange(0, choice_of_range+1)
        guess = int(input("Enter your guess : "))
        

        while (guess != computer_guess):
            
            if guess < computer_guess :
                
                print("Your guess seems to be smaller than the number.")

            elif guess > computer_guess :
                
                print("Your guess seems to be higherer than the number.")

            else :
                
                print("Woohoo! You have guessed the number correctly.")
            guess = int(input("Enter your guess : "))
            count += 1
        else :
            print("Enter a valid number bigger than 0.")
    if count <= 5:
            print("WOW1  You Won !!! \nYou guessed the number within ", count+1, "times.")
    else :
            print("You lose. Try better next time. You guessed the number within ", count+1, "times.")

    playing = input("Do you want to continue playing the game ? : ").upper()
