import nltk
import random

# Download the wordlist from NLTK
nltk.download("words")
from nltk.corpus import words

def load_word_list():
    english_word_list = words.words()
    five_letter_words = [word.lower() for word in english_word_list if len(word) == 5]
    return five_letter_words

def choose_query(word_list):
    return random.choice(word_list)

def check_guess(query, guess):
    feedback = ''
    guess = list(guess)
    remaining_query = list(query)  # Maintain a list of remaining letters in the query
    correct_positions = set()
    correct_letters = set()
    correct_position_letter = set()

    for i in range(len(query)):
        if guess[i] == query[i]:
            feedback += guess[i].upper()
            correct_positions.add(i)
            #correct_letters.add(guess[i])
            correct_position_letter.add(guess[i])
            guess[i] = '_'
            remaining_query[i] = ' '  # Use a space to mark correctly guessed positions
        else:
            feedback += '_'

    for i in range(len(query)):
        if guess[i] in remaining_query:
            #if guess[i] in correct_letters:
            correct_letters.add(guess[i])
            #correct_positions.add(i)  # Mark the position as correct
            remaining_query[remaining_query.index(guess[i])] = ' '  # Mark the letter as correct
            feedback = feedback[:i] + guess[i].lower() + feedback[i + 1:]
            guess[i] = "_"

    #repeating_letters = [char for char in guess if guess.count(char) > 1]
    #for letter in repeating_letters:
        #matching_positions = [pos for pos, char in enumerate(query) if char == letter]
        #if any(pos in correct_positions for pos in matching_positions):
            #for i in range(len(guess)):
                #if guess[i] == letter and i not in matching_positions:
                    #feedback = feedback[:i] + guess[i].lower() + feedback[i + 1:]
                    #break
        #else:
            #first_appearance = guess.index(letter)
            #feedback = feedback[:first_appearance] + letter.lower() + feedback[first_appearance + 1:]

    return feedback


def is_valid_english_word(word):
    return word in load_word_list()

def play_wordle():
    english_word_list = load_word_list()

    while True:
        query = choose_query(english_word_list)
        tries = 6
        print("\nWelcome to Wordle! Guess the 5-letter word.")

        while tries > 0:
            guess = input(f"\nTries left: {tries}\nEnter your guess: ").strip().lower()

            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue

            if not is_valid_english_word(guess):
                print("Please enter a valid English word.")
                continue

            if guess == '0':
                print("You cannot enter a 0-word input.")
                continue

            if guess == query:
                print(f"Congratulations! You've guessed the word: {query}")
                break

            feedback = check_guess(query, guess)
            print("Evaluation:", ' '.join(feedback))

            tries -= 1

        if tries == 0:
            print(f"\nOut of tries! The word was: {query}")

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    play_wordle()
