#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
# Function 1
# • Write a for loop that returns all the animals from the NE Farm!
for animal in farms[0]["agriculture"] : print(animal)
# Function 2
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
farm = str(input("Please choose between farms NE, W, and SE.\n"))
if farm=="NE": 
    for animal in farms[0]["agriculture"] : print(animal)
elif farm=="W": 
    for animal in farms[1]["agriculture"] : print(animal)
elif farm=="SE": 
    for animal in farms[2]["agriculture"] : print(animal)
else : print("Your input is invalid\n")
# Function 3
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
farm = str(input("Please choose between farms NE, W, and SE and I'll show you animals on the farm chosen.\n"))
if farm=="NE": 
    for animal in farms[0]["agriculture"] : print(animal)
elif farm=="W": 
    for animal in farms[1]["agriculture"] : print(animal)
elif farm=="SE": 
    print("carrots, celery")
else : print("Your input is invalid\n")

