soda = 4
def drink_soda():
    soda = 5
    print(f"lets drink some soda today {soda}")# local scope
drink_soda()
print(f"lets drink some soda today {soda}") #global scope 


#water = 34  now if we dont have this one ,it can not work becoz the one 
# in the function is not accesible from the main function and is know as 
# local variable   # but when if we leave it open then the line at 16
# will work becoz the one at 14 is accesible from the main function and is
# know as global variable
def drink_water():
    water = 45
    print(f"have you taken water  {water}")
drink_water()
#print(f"have you taken water  {water}")


