# Import random module
import random

# Create a variable that will hold random number
random_number = random.randint(1,100)
print(random_number)

# Print introduction to the game and explain the rules
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# Create a list to store quesses
guess_list = [0]

# Create a while loop that asks for a valid guess
while True:
    guess = int(input("Please provide your guess: "))

    if guess < 1 or guess > 100:
        print("Out of Bounds! Please try again: ")
        continue
    break

