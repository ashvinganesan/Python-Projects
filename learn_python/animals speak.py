class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.previous_weight = weight

    def add_to_weight(self, amount):
        self.previous_weight = self.weight
        self.weight += amount
    
    def speak(self):
        pass
       
class Dog(Pet):
    def speak(self):
        return "Woof"

class Cat(Pet): 
    def speak(self):
        return "Meow"
class Iguana(Pet):
    def speak(self):
        return "Zzz..."
class Mouse(Pet):
    def speak(self):
        return "Squeek"

ctd = Dog('Cooper', 60)
mtd = Dog('Murphy', 70)

print(ctd.name + ', the '+ ctd.__class__.__name__ + ', says ' + ctd.speak()+ " and he is " + str(ctd.weight) + " pounds") 
print(mtd.name + ', the dog, says ' + mtd.speak()+ " and he is " + str(mtd.weight) + " pounds") 

mtd.add_to_weight(10)
ctd.add_to_weight(10)


print(mtd.name + ', the dog, says ' + mtd.speak()+ " and he was " + str(mtd.previous_weight) +', but he is now ' + str(mtd.weight) + " pounds")
print(ctd.name + ', the dog, says ' + ctd.speak()+ " and he was " + str(ctd.previous_weight) +', but he is now ' + str(ctd.weight) + " pounds")





pltg = Cat('Pluto', 20)
petg = Cat('Pepper', 12)

print (pltg.name + ', the cat says ' + pltg.speak()+ " and he is " + str(pltg.weight) + " pounds")
print (petg.name + ', the cat says ' + pltg.speak()+ " and she is " + str(petg.weight) + " pounds")

pltg.add_to_weight(3)
petg.add_to_weight(-2)

print(pltg.name + ', the cat, says ' + pltg.speak()+ " and he was " + str(pltg.previous_weight) +', but he is now ' + str(pltg.weight) + " pounds")
print(petg.name + ', the cat, says ' + petg.speak()+ " and she was " + str(petg.previous_weight) +', but she is now ' + str(petg.weight) + " pounds")

