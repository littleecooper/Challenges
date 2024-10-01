boxes_of_eggs = input("How many boxes of eggs do you have?\n")
eggs_in_box = input("How many eggs are in each box?\n")

eggs_in_fridge = int(boxes_of_eggs) * int(eggs_in_box)

#print(eggs_in_fridge) This was to test if both my inputs worked.

eggs_per_omelette = 4

amount_of_omelette = eggs_in_fridge / eggs_per_omelette

output = "You can make " + str(amount_of_omelette) + " omelettes"

print(output)

