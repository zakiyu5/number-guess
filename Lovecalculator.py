print("Welcome to our love calculator")
Name1 = input("Enter the Name::::")
Name2 = input("Enter the Name:::")
combined_names = Name1+ Name2
Lower_names = combined_names.lower()
t = Lower_names.count("t")
r = Lower_names.count("r")
u = Lower_names.count("u")
e = Lower_names.count("e")
first_name =  t+r+u+e

l = Lower_names.count("l")
o = Lower_names.count("o")
v = Lower_names.count("v")
e = Lower_names.count("e")
second_name = l+o+v+e

final = int(str(first_name)+str(second_name))
if final <=10 and final > 100:
  print(f"Your score is {final}, you go together like coke and mentos.")
elif final > 40 and final < 50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"your score is {final}")
