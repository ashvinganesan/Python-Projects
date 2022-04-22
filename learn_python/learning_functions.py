def print_two(arg1, arg2):
    print('arg1 is %s and arg2 is %s' % (arg1, arg2))
          
def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothin'.")


print_two("Appa", "Amma")
print_one("last")
print_none() 


          


def compute_int(principle, interest_rate, years):
    multiplier = 1 + interest_rate/100
    final_amount = principle * (multiplier**years)
    interest = final_amount - principle
    return interest

p = 1000; r = 10; years = 11
for x in range (1, years):
    answer = compute_int(p,r,x)
    print('Your interest on %3d at a rate %3d for %3d years is %s' % (p, r, x, answer))

print()
print('-' * 50)
print()
p = 1000; r = 11; years = 10
for x in range (1, r):
    answer = compute_int(p,x,years)
    print('Your interest on %3d at a rate %3d for %3d years is %s' % (p, x, years, answer))

