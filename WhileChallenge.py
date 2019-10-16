import random

highest = 10
answer = random.randint(1, highest)

print("Please enter a number between 1 and {} (zero to quit)".format(highest))
guess = int(input())
while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input())

if guess != 0:
    print("You guessed correctly!")
    

