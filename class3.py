import random

x = random.randint(1, 10)
guess = int(input("Enter an integer from 1 to 10: "))

while x != "guess":
  print
  if guess < x:
    print ("guess is too low")
    guess = int(input("Enter an integer from 1 to 10: "))
  elif guess > x:
    print ("guess is too high")
    guess = int(input("Enter an integer from 1 to 10: "))
  else:
    print ("ok")
    break