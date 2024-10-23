# Guess the animal

# A random animal is chosen from the list. (MET THIS) The user guesses an animal, they are told if they
# guessed the correct animal or not, if they guess the same animal again, they are told that they already guessed that animal
# if they guess right, they win

import random

animals = [
    "sheep",
    "cow",
    "pig",
    "dog",
    "cat",
    "tiger",
    "lion",
    "parrot"
]

#random_animal = animals.randint([0,10])
#print(random_animal)    I was experimenting with the .randint() function here and realised that this can only help with integers and not items in a list. 

#print(random.choice(animals))  This was helpful but I realised I needed to assign the random choice
# a variable name so this is why I had written the code below

random_animal = random.choice(animals)
# print(random_animal) # This was to test that the above code worked. Do not want to keep this
#otherwise the player will see what random animal the computer has picked
#guessed_animal = -1

picked_animal = input("Guess an animal from the following list: Sheep, Cow, Pig, Dog, Cat, Tiger, Lion, parrot").lower().strip()

#chosen_animal = int(input("Not quite right, choose again"):

while random_animal != picked_animal:
    print("WRONG!")

    if animals.count(picked_animal) == 0:
      print("That is not an option, choose wisely next time")

    picked_animal = input("Would you like to choose again?").lower().strip()
    # print(picked_animal)

  #  print(random_animal)
 # break

if random_animal == picked_animal:
    print("Congratulations, You guessed the animal correctly")
    #  break

# else:   This was created before I had tidied up my code
#       print("That is not an option, choose wisely next time")
#       input("Which animal would you like to choose?")