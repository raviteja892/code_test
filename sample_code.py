import random

def guess_the_number():
    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the 'Guess the Number' game!")
    print("I've selected a random number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Try a higher number.")
            elif guess > secret_number:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the number ({secret_number}) in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
