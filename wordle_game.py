import random

def generate_word():
    word_list = ["apple", "table", "chair", "house", "mouse", "robot", "piano", "zebra", "blank", "prank", "black"]
    return random.choice(word_list)

def compare_words(word, guess):
    green_count = 0
    yellow_count = 0
    word_dict = {}
    guess_dict = {}

    for i in range(len(word)):
        if word[i] == guess[i]:
            green_count += 1
        else:
            if word[i] not in word_dict:
                word_dict[word[i]] = 1
            else:
                word_dict[word[i]] += 1

            if guess[i] not in guess_dict:
                guess_dict[guess[i]] = 1
            else:
                guess_dict[guess[i]] += 1

    for letter in guess_dict:
        if letter in word_dict:
            yellow_count += min(guess_dict[letter], word_dict[letter])

    return green_count, yellow_count

def play_wordle():
    word = generate_word()
    attempts = 0
    print("Welcome to Wordle!")
    print("Green means valid alphabet at correct position. \nYellow means valid alphabet at incorrect position.")
    while attempts < 6:
        guess = input("Enter your guess: ")
        guess = guess.lower()

        if len(guess) != len(word):
            print("Invalid input! Please enter a word with 5 letters.")
            continue

        green_count, yellow_count = compare_words(word, guess)

        if green_count == len(word):
            print("Congratulations! You guessed the word correctly!")
            break

        print(f"Your guess: {guess}")
        
        print(f"Green squares: {green_count}")
        print(f"Yellow squares: {yellow_count}")
        print("-----------------------------")

        attempts += 1

    if attempts == 6:
        print(f"Sorry, you ran out of 6 attempts! The word was '{word}'.")

play_wordle()
