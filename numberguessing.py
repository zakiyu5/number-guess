from random import randint
#from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5
turn = 0
# function to check usersguess with actual actual guess
def check_answer(user_guess , actual_input):
    if user_guess >  actual_input:
        print("Too high")
        return turn -1
    elif user_guess < actual_input:
        print("Too low")
        return turn - 1
    else:
        print(f"You got it right!,the answer was {actual_input}")
# difficult 
def set_difficult():
        difficult = input("Choose a difficult level: easy, hard ")
        if difficult == "easy":
             return EASY_LEVEL
        else:
             return HARD_LEVEL

        # function to generate random number between 1 and 100
        def generate_random_number():
            return randint(1, 100)
        # generate random number between 1 and 100
        random_number = generate_random_number()
        # call check_answer function with user_guess and random_number as arguments
        check_answer(user_guess, random_number)
def game():
   # print(logo)
    # for random numbers 
    print("welcome to the number guesing game ")
    print("am thinking of a number between 10 to 100")
    answer = randint(10 , 100)
    # function to set difficult
    def difficult():
        print("choose a difficult level ")

    turns = set_difficult()
    print(f"you have {turns} remaining to finish the game ")
    # LET THE USER GUESS A NUMBER 
    guess = 0
    while guess != answer:
        
        guess = int(input("enter your guess "))
        check_answer(guess,answer,turns)
    if turns ==0:
         print("you have run out of turns ")
    elif guess ==answer:
         print("guess again ")

game()