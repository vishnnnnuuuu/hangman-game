import random

def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    word_display = ['_'] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0 and '_' in word_display:
        print("\nCurrent word:", ' '.join(word_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_display[index] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
    
    if '_' not in word_display:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nSorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
