from random import randint
#from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to check user's guess with the actual number
def check_answer(user_guess, actual_input, turns):
    if user_guess > actual_input:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_input:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it right! The answer was {actual_input}.")
        return turns

# Function to set difficulty level
def set_difficulty():
    difficulty = input("Choose a difficulty level: easy or hard: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

# Function to handle the game logic
def game():
    #print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    turns = set_difficulty()
    
    guess = 0
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses. You lose.")
        elif guess != answer:
            print("Guess again.")

game()
