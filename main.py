import random
import string


# -----------------------------------------
# Number Guessing Game
# -----------------------------------------
def number_guessing_game():

    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")

    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    secret_number = random.randint(1, 100)

    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("\nCongratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)

            score = (max_attempts - attempts + 1) * 10

            print("Your score:", score)

            return

    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Your score: 0")


# -----------------------------------------
# Word Counter
# -----------------------------------------
def word_counter():

    print("\n================================")
    print("       WORD COUNTER")
    print("================================")

    filename = input("Enter text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError:
        print("File not found!")
        return

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split text into words
    words = text.split()

    # Count total words
    total_words = len(words)

    print("\nTotal number of words:", total_words)

    # Word frequency
    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\n===== Word Frequency =====")

    for word, count in sorted(frequency.items()):
        print(word, ":", count)


# -----------------------------------------
# Main Menu
# -----------------------------------------
def main():

    while True:

        print("\n========================================")
        print(" NUMBER GUESSING GAME & WORD COUNTER")
        print("========================================")

        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("\nThank you for using the program!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# -----------------------------------------
# Start Program
# -----------------------------------------
if __name__ == "__main__":
    main()