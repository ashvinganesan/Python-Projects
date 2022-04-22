import random

number = random.randint(1, 100)

score = 0


numb1 = 1
numb2 = 100
while True:
    print("guess a number from %s to %s lowest score wins :)" % (numb1, numb2))
    guess = input()
    i = int(guess)

    if  i > numb2:
        print("guess lower so that it is in the range")
    if  i < numb1:
        print("guess higher so that it is in the range")
    
    if i == number:
        score = score + 1
        print("you got it correct your score was %s" % score)
        break
    if i > number:
        if not i  > numb2:
            print("guess lower")
            score = score + 1
            if i < numb2:
                numb2 = i
        

    
  
    if i < number:
        if not i < numb1:
            print("guess higher")
            score = score + 1
            if i > numb1:
                numb1 = i
    
    

    
