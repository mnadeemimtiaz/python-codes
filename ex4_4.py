import random
number = random.randint(1,10)
guessused = 1
while guessused < 60:
   guess = int(input("Guess your number :"))
   if guess > number:
      print("Too High")
   elif guess < number:
      print("Too low")
   else:
      print("Correct")
      break