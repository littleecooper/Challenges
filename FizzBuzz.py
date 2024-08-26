# FizzBuzz


# Given a number, print every number up to the inputted number replacing multiples of 3 with fizz,
# and multiples of 5 with buzz. multiples of both with fizzbuzz

print("Enter a number for fizzbuzz")
number = input()

for loop_number in range(1, int(number)):

    if loop_number % 3 == 0 and loop_number % 5 == 0:
        print("FizzBuzz")

    elif loop_number % 5 == 0:
        print("Buzz")

    elif loop_number % 3 == 0:
        print("Fizz")

    else:
        print(loop_number)
