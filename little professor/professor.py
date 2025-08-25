# EEE for incorrect answer(or not even an int), after three times display the correct answer
# prompt user for a level "n", from 1 to 3, reprompt user if input not in [1, 2, 3]
# randomly generate 10 math questions in format of "X + Y =", X and Y are non-negative integer with n digits.
# ultimately output the user’s score: the number of correct answers out of 10
# get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
# generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
# randint, randrange

import random

def main():
    score = 0

    n = get_level()

    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for _ in range(3):
            try:
                global answer
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                answer = None
                print("EEE")
            else:
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")

        if answer != x + y or answer == None:
            print(f"{x} + {y} =", x + y )

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level

def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    else:
        return random.randrange(100, 1000)

if __name__ == "__main__":
    main()
