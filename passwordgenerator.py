#my python password Generator

import random
import string
print("welcome to the pypassword Generator ! ")
letters_counts = int(input("How many letters will you like in your password \n"))
symbols_counts =  int(input("how many symbols do you like in your password  \n"))
numbers_counts = int(input("how many numbers do you like in your password  \n"))

letters = string.ascii_letters
symbols  = string.punctuation
numbers =  string.digits

password_list = []
for _ in range(letters_counts):
  password_list.append(random.choice(letters))
for _ in range (symbols_counts):
  password_list.append(random.choice(symbols))
for _ in range (numbers_counts):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)
print(f"here is your : {password}")

