import random

def info(in_array):
    print("find out how to add subtract multiply or divide while using these four numbers  to get 24")
    print("the numbers are:")
    print(in_array[0], in_array[1], in_array[2], in_array[3])
    print("Input your answer:")

def random_numbers():
    out = []
    my_max = 13
    for _x in range(1,5):
        out.append(random.randint(1, my_max))
        if out[-1] > 9:
            my_max = 10
    return out
 

playing = True
while playing:
    print("******* playing loop")
    res = random_numbers() 
    guessing = True
    while guessing:
        print("******* guessing loop")
        info(res)
        guess = input()
        i = eval(guess)
        
        if i == 24:
            print("You Win")
            print("do you want to play again")  
            yes_no = input()
            if yes_no == "no":
                playing = False
                guessing = False
        else:
            print("Wrong guess do you want to try guessing again or quit?")
            yes_no = input()
            if yes_no == "yes":
                continue
            elif yes_no == "quit":
                playing = False
                guessing = False
            else:
                guessing  = False 
         
