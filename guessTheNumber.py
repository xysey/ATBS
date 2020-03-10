import random

number = random.randint(1, 20)
guesses = 0

print("I'm thinking of a number 1 and 20.")

while True:
    print("Take a guess")
    guesses = guesses + 1
    guess = input()
    if int(guess) == number:
        print("Good job you've guess my number in " + str(guesses) + " guesses.")
        break
    elif int(guess) > number:
        print("Your guess is too high.")
    elif int(guess) < number:
        print("Your guess is too low.")
