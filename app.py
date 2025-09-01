import random
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print(" Hurrayyyy! You guessed it right!")
else:
    print(f" Wrong guess. The correct number was {secret_number}.")
