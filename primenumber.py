def is_prime(num):
    #num = int(input("enter your number od interest  "))
    if num < 2:
        return False
    for i in range(2 ,int(num**0.5)+1):
        if num %i ==0:
            return False
    return True
    
num = int(input("enter your number of interest  "))
result = is_prime(num)
print(result)
    
    