# Create a Ninja class with ninja attributes
# attributes: firt_name, last_name, pet,treats,pet_food,pet(this attribut will be the class Pet)

class Ninja:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.treats = data["treats"]
        self.pet_food = data["pet_food"]
        self.ninja_pet = None

# implement walk methods: walks the ninja's pet invoking the pet play()method
    def walk(self):
        print(f"Let's go for a walk!")
        self.ninja_pet.play()
        return self

# implement feed methods: feed the ninja's pet invoking the pet eat()method
# print the initial energy  level first, 
# if the energy is low than 10, meaning it's very hungry
# feed all the foods in the list, here we will invoke the pet.eat()method, 
# energy level increased, and print out the increased value
# if the energy level is more than 10, then go to play
    def feed(self):
        print(f"{self.ninja_pet.pet_name} energy level is {self.ninja_pet.pet_energy}","\n")
        if self.ninja_pet.pet_energy < 10:
            for food_count in range (0,len(self.pet_food)):
                print(f"{self.ninja_pet.pet_name} is hungry")
                print(f"Feeding {self.ninja_pet.pet_name} {self.pet_food[food_count]}")
                self.ninja_pet.eat()
            print(f"Oh no!! You need more pet foods!!","\n")
        else:
            print(f"{self.ninja_pet.pet_name} is full now. Let's play","\n")
        return self

# implement walk methods: walks the ninja's pet invoking the pet play()method
    def bathe(self):
        print(f"Let's take a bath! ")
        self.ninja_pet.noise()
        print(f"{self.ninja_pet.pet_name} is clean now","\n")
        return self

# print method
    def print_statement(self):
        print(f"{self.first_name} {self.last_name} has a {self.ninja_pet.pet_type}","\n")


