import random
from subprocess import call

GREETING = "Hello"

adj= ['happy', 'mad', 'sad', 'kind', 'amazing', 'great', 'stinky']
fam= ['Ashvin','Akash','Elango','Gita']

def speak(message, name):
    msg = GREETING + ' ' + message + ' ' + name
    print(msg)
    call(["say", msg])

for x in range (0,10):
    speak(random.choice(adj), random.choice(fam))
    
