import random

def guess_the_number(difficulty):
    if difficulty == "easy":
        lower_limit, upper_limit = 1, 50
    elif difficulty == "medium":
        lower_limit, upper_limit = 1, 100
    elif difficulty == "hard":
        lower_limit, upper_limit = 1, 200
    else:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        return

    print(f"Welcome to the {difficulty.capitalize()} Level of the Number Guessing Game!")
   
    # Generate a random number based on the chosen difficulty
    secret_number = random.randint(lower_limit, upper_limit)
   
    attempts = 0

    while True:
        try:
            # Get user input for the guess
            user_guess = int(input(f"Guess the number (between {lower_limit} and {upper_limit}): "))
            attempts += 1

            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    difficulty_level = input("Choose the difficulty level (easy, medium, or hard): ").lower()
    guess_the_number(difficulty_level)