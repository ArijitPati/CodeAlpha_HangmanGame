import random

# 5 random words
words=['train','bus','tram','plane','ship']     

correctWord=random.choice(words)

guessedLetter=['_']*len(correctWord)

guessedChar=[]

maxWrong = 6
wrong = 0

# Game introduction
print("Welcome to Hangman Game!")               
print("Guess the word, one letter at a time.")
print(f"You have {maxWrong} incorrect guesses.")

# Game loop
while((wrong<maxWrong)and '_' in guessedLetter):    
    print("\nWord: ", ' '.join(guessedLetter))
    print("Guessed letters: ", ', '.join(guessedChar))
    print("Wrong guesses left: ", maxWrong-wrong)

    guess = input("Enter a letter: ").lower()

    # Checks for a invalid input
    if not guess.isalpha() or len(guess) != 1:           
        print("Please enter a single alphabet letter.")
        continue

    # Checks for a already guessed letter
    if guess in guessedChar:
        print("You already guessed that letter.")
        continue

    guessedChar.append(guess)

    # Checks for a correct guess
    if guess in correctWord:
        print("Good guess!")

        # Replaces the correct letter in the dash 
        for i in range(len(correctWord)):
            if correctWord[i] == guess:
                guessedLetter[i] = guess
    else:
        print("Wrong guess!")
        wrong += 1

# Game over and message displayed
if '_' not in guessedLetter:
    print("\nCongratulations! You guessed the word:", correctWord)
else:
    print("\nGame Over! The word was:", correctWord)