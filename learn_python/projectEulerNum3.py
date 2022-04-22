


def largest_prime_factor(number):
    largest_prime = 1
    is_prime = False
    for x in range(300425737572 , 2, -1):
        is_prime = False
        for y in range(2,x-1):
            if (x % y == 0):
                is_prime = False
                break
        else:
            is_prime = True
        if is_prime:
            if number % x == 0:
                largest_prime = x
                print(largest_prime)
                break
        

largest_prime_factor(600851475143)
