print("Welcome to Tresure Island.")
print("Your Mission is to find the tresure ")

choice_1 = input('You are at cross road ,Where do you want to go? Type "left" or "Right" \n ')

if choice_1 == "left":
  choice_2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice_2 == "wait":
    choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice_3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice_3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice_3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
