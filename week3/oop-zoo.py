class Animal():
    def __init__(self, name, species, sound="generic animal sound"):
        self.name = name
        self.species = species
        self.sound = sound
# added sound as an attribute rather than hard coding for each instance
    def speak(self):
        return(f'{self.sound}')
class Mammal(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def give_birth(self):
        return "It has given birth!"
class Bird(Animal):
    def __init__(self, wingspan, **kwargs):
        self.wingspan = wingspan
        super().__init__(**kwargs)
class Reptile(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def bask_in_sin(self):
        print("The reptile is basking in the sun.")
class Primate(Mammal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def climb_trees(self):
        print("The primate is climbing trees.")
class Marsupial(Mammal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def carry_baby(self):
        print("The marsupial is carrying the baby.")

mammal1 = Mammal(name = "Harry", species = "animal", sound = "WARGH")
marsupial1 = Marsupial(name = "Alfonse", species = "marsupial", sound = "ek-ek" )
bird1 = Bird(name = "Flip", species = "bird", sound = "cuckoo", wingspan= 8 )

print(mammal1.speak())
print(marsupial1.speak())
print(marsupial1.name)
marsupial1.carry_baby()
print(bird1.wingspan)
print(mammal1.give_birth())