import random

number = random.randint(1, 20)

print("I'm thinking of a number 1 and 20.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        break

if guess == number:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope, The number I was thinking of was " + str(number))
