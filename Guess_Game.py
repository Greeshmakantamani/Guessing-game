# Importing random module to generate random numbers
import random as r

# Loop to allow playing the game multiple times until the user quits
while True:
    comp = input("Can you tell your name: ")       # Asking the user for their name
    print(f"Hey {comp}! Today let's play 'The Guessing Game'")  # Greeting the user

    # Generate a random number between 1 and 100 (inclusive)
    guess_num = r.randint(1, 100)

    attempt = 0            # Counter to track the number of attempts used
    max_attempts = 10      # Maximum number of chances allowed to guess
    print("The values are in range of 1 to 100")

    # Loop runs until attempts are less than the allowed max attempts
    while attempt < max_attempts:
        try:
            # Ask user to enter their guessed number
            user_num = int(input("Enter a number: "))

            # Validate input range (must be between 1 and 100)
            if user_num < 1 or user_num > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempt += 1   # Increase attempt count after each valid input

            # Check conditions to guide the user
            if user_num > guess_num:
                print("Think Low!")   # User guessed too high
            elif user_num < guess_num:
                print("Think High!")  # User guessed too low
            else:
                # Correct guess
                print("🎉 You GOT IT!!")
                print(f"It took you {attempt} attempts.")
                break  # Exit the loop since the game is won
        except ValueError:
            # Handle non-integer input (like letters or symbols)
            print("Please enter a valid number.")

    else:
        # If the loop completes without breaking, it means all attempts are used
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {guess_num}.")

    # Ask if the player wants to play again
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing! 👋")
        break  # Exit the outer loop and end the game
