# Create a Pet class with the pet attributes given below:
# name, type, tricks, health, energy

class Pet:
    def __init__(self,data):
        self.pet_name = data["pet_name"]
        self.pet_type = data["pet_type"]
        self.pet_tricks = data["pet_tricks"]
        self.pet_health = 0
        self.pet_energy = 0

# implement the sleep method:
# increase the energy by 25
    def sleep(self):
        print(f"Zzzzz")
        self.pet_energy +=25
        print(f"{self.pet_name} is awake now. It's energy level is {self.pet_energy}")
        print(f"It's health level is {self.pet_health}","\n")
        return self

# implement the eat method:
# increase the energy by 5
# increase the health by 10
    def eat(self):
        self.pet_energy += 5
        self.pet_health += 10
        print(f"{self.pet_name} is full now. It's energy level is {self.pet_energy}")
        print(f"It's health level is {self.pet_health}","\n")
        return self

# implement the play method:
# increase the health by 5
    def play(self):
        self.pet_health +=10
        self.pet_energy -=10
        print(f"{self.pet_name} is happy now.")
        print(f"It's health level is {self.pet_health}","\n")
        return self

# implement the noise method
# print out the pet's sound, in this case, set it as dog bark
    def noise(self):
        print(f"Woof!!Woof!!Woof!!")
        return self

# Bonus: Use  inheritance to create sub classes of pets
class Cat(Pet):
    def __init__(self,data):
        super().__init__(data)
        self.pet_attitude = data["pet_attitude"]

# change the noice into cat
    def noise(self):
        print(f"Miao!Miao!Miao!!")
        return self