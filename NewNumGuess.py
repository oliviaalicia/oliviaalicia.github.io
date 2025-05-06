import random

# Constants
MAX_HEARTS = 4
MIN_NUMBER = 1
MAX_NUMBER = 10

def play_game():
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    hearts = 0

    while hearts < MAX_HEARTS:
        try:
            guess = int(input(f"\nGuess a number between {MIN_NUMBER}-{MAX_NUMBER} (0 to exit): "))
            
            if guess == 0:
                print("Exiting the game.")
                return False  # False means the player didn’t want to replay

            if guess > answer:
                print("Too high!")
            elif guess < answer:
                print("Too low!")
            else:
                print(f"🎉 Congratulations! The answer was {answer}")
                return ask_replay()  # Return True/False based on replay

            hearts += 1
            print(f"Lives remaining: {MAX_HEARTS - hearts}")

        except ValueError:
            print("Please enter a valid integer.")
    
    print(f"💀 Game over! The answer was {answer}")
    return ask_replay()

def ask_replay():
    while True:
        choice = input("\nPlay again? (Y/N): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'Y' or 'N'.")

# Main loop
def main():
    print("**************************")
    print(" Welcome to Number Guess ")
    print("**************************")
    print(f"Info: You have {MAX_HEARTS} lives. Press 0 to exit anytime.")
    
    while True:
        if not play_game():
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()