import random
number=random.randint(1,100)
chance=7
print("welcome to number guessing game")
for i in range(chance):
    guess=int(input("enter your guess (1=100:)"))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("congratulations! you guess it right")
        break 
else:
    print("your guess is wrong the  correct number is",f'{number}')   