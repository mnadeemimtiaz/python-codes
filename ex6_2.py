import random

def throw_dice(nsides):
    return random.randint(1, nsides)

def result():
    nsides = int(input("Number of DICE sides = "))

    while True:
        dice_r = throw_dice(nsides)
        print(f"The result is: {dice_r}")
        if dice_r == nsides:
            break
result()
