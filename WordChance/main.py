from tkinter import *
import random

def load_dictionary(file_path):
    '''
    Open file and strip each line
    '''
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    '''
    returns guess in guesses
    '''
    return guess in guesses

def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m"+ guess[i]
    return str + "\033[0m"

def wordle(guesses, answers):
    while True:
        print("\n\n\t\tWelcome to WordChance! You have 6 chances to guess the word I'm thinking. \n The word that I'm thinking of has 5 letters.")
        print("\t\tIf the letters in your guess are in the correct spot they will turn green.")
        print("\t\tIf the letters in your guess are in the word, but not in the correct spot, they will turn yellow.")
        choice = input("\t\tPress 1 to continue, 0 to exit: ")
        if choice == '0':
            return False
            break
        else:
            print("Great, Let's Go!")
        print('\t\t\t\t**********')

        secret_word = random.choice(answers)

        attempts = 1
        max_attempts = 6

        while attempts <= max_attempts:
            guess = input("Enter Guess #" + str(attempts) + ": ").lower()
            if not is_valid_guess(guess, guesses):
                print("Invalid guess. Please enter English word with 5 letters.")
                continue
            if guess == secret_word:
                print("Congratulations! You guessed the word: ", secret_word)
                break
            
            attempts += 1
            feedback = evaluate_guess(guess, secret_word)
            print(feedback)

        if attempts > max_attempts:
            print("Game over. The secret word was: ", secret_word)


guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

wordle(guesses, answers)
