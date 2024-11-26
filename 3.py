import random

def scramble_word(word):
    return ''.join(random.sample(word, len(word)))

def word_scramble_game():
    
    words = ["apple", "banana", "cherry", "orange", "grape", "peach"]
    
    
    original_word = random.choice(words)
    
    
    scrambled_word = scramble_word(original_word)
    
    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print("You have 5 attempts.")
    
    attempts = 5
    while attempts > 0:
        
        guess = input("Enter your guess: ")
        
        
        if not guess:
            print("Invalid input! Please enter a word.")
            continue
        
        if guess == original_word:
            print("Congratulations! You guessed the correct word!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! Try again. You have {attempts} attempts left.")
            else:
                print(f"You’re out of attempts! The correct word was: {original_word}")


word_scramble_game()
