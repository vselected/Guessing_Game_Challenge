def guessinggame():

    # Import random module
    import random

    # Print introduction to the game and explain the rules
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")

    # Create a variable that will hold random number
    random_number = random.randint(1, 100)

    # Create a list to store guesses
    guess_list = [0]

    # Create a while loop
    while True:
        guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

        # Check if guess is valid
        if guess < 1 or guess > 100:
            print("Out of Bounds! Please try again: ")
            continue

        # Compare player's guess to our random number
        if guess == random_number:
            print(f"Congratulations you guessed it in only {len(guess_list)} guesses!")
            break

        # Add guess to the guesses list
        guess_list.append(guess)

        if guess_list[-2]:
            # Check if guess is better that previous guess
            if abs(random_number - guess) < abs(random_number - guess_list[-2]):
                print("WARMER!")
            else:
                print("COLDER!")
        else:
            # Check if player's guess is within 10
            if abs(random_number - guess) <= 10:
                print("WARM!")
            else:
                print("COLD!")

# Start the game
guessinggame()