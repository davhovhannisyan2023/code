import random

def play_game():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    num_guesses = 0
    while True:
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            break

play_game()
