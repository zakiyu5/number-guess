import random

print("hello world")

# Initialize an empty list x to store numbers
x = []

# Get the number of inputs from the user
y = int(input("Enter the number of preferred numbers you will input: "))

# Collect 'y' numbers from the user and add them to the list x
for _ in range(y):
    number = int(input("Enter your preferred number: "))
    x.append(number)

# Choose a random number from the list x
chosen = random.choice(x)

# Get the target number from the user
target = int(input("Enter your target: "))

# Check if the target is equal to the chosen number
if target == chosen:
    print("You have passed")
else:
    print("Try again later")

print(f"Game over. Here is your final chosen value: {chosen}")
