# Guess the number

# A random number is assigned. The user guesses a number, if they are too high, they are told
# they are too high and they guess again, vice versa for too low.

import random

random_number = random.randint(0,5)

#print(random_number)     This was included to test my random.randint() function worked and if the while loop would break if I guessed the number correctly. 3

picked_number = int(input("Pick a number between 1 and 5"))


while random_number != picked_number:
    picked_number = input("Not quite right, guess again")
    # insert your code here

if picked_number == random_number:
    print("Congratulations, you guessed the number!")
