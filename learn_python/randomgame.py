import random

number = random.randint(1,100)

numb1 = 1
numb2 = 100
while True:
    print("guess a number from %s to %s :)" % (numb1, numb2))
    guess = input()
    i = int(guess)
    if i == number:
        print("you got it correct")
        break
    if i > number:
        numb2 = i
        print("guess lower")

    
  
    if i < number:
        numb1 = i
        print("guess higher")
    
    

    
