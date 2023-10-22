import random
numb_dice = int(input("Number of dices to roll? "))
total = 0
for _ in range(numb_dice):
    diceroll = random.randint(1, 6)
    total += diceroll
print(f" {numb_dice} dice rolled and sum = {total}")