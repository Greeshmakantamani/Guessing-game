import random as r

while True:
    comp = input("Can you tell your name: ")
    print(f"Hey {comp}! Today let's play 'The Guessing Game'")

    guess_num = r.randint(1, 100)
    attempt = 0
    max_attempts = 10
    print("The values are in range of 1 to 100")

    while attempt < max_attempts:
        try:
            user_num = int(input("Enter a number: "))

            if user_num < 1 or user_num > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempt += 1

            if user_num > guess_num:
                print("Think Low!")
            elif user_num < guess_num:
                print("Think High!")
            else:
                print("🎉 You GOT IT!!")
                print(f"It took you {attempt} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {guess_num}.")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing! 👋")
        break
