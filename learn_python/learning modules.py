class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
harry = Pet('harry', 'hippo')
import copy

harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

carrie = Pet('carrie', 'chimera')
billy = Pet('billy', 'bogil')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)

sally = Pet('sally', 'sphinx')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))



 
