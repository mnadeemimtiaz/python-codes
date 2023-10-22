import random

def throw_dice():
    return random.randint(1, 6)
def result():
    while True:
        dice_result = throw_dice()
        print(f"The result is: {dice_result}")
        if dice_result == 6:
            break
result()