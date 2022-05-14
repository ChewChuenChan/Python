# Bonus: use modules to separates out the classes into different files

from ninja import Ninja
from pet import Pet ,Cat

# Make an instance of Ninja

alice = Ninja({
    "first_name":"Alice",
    "last_name":"Chan",
    "treats":["carrots","watermelon"],
    "pet_food":["chicken","beef"],
    "ninja_pet" : "alice_pet"
})

alice_pet= Pet({
    "pet_name":"Meimei",
    "pet_type":"Siberian Husky",
    "pet_tricks":["go potty","sit still"]
})
# assign them an instance of a pet to the pet attribute
alice.ninja_pet=alice_pet

# Have the Ninja feed, walk, and bathe their pet
alice.feed().feed().walk().bathe()

# Testing for inheritance 
kitty_cat =Cat({
    "pet_name":"Gray",
    "pet_type":"American Shorthair",
    "pet_tricks":["fetch","come"],
    "pet_attitude" : "friendly"
})
kitty_cat.eat().noise()