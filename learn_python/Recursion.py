
def factorial(n):
    print("factorial %s called" % n)
    if n == 1:
        return 1
    return n * factorial(n-1)
    

print(factorial(5))



def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(9))
    

 



