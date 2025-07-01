import random
# Levels of the difficulty
def get_difficulty():
    print("🎮 Welcome to Hangman!")
    print("\nSelect Difficulty Level:")
    print("1. Easy   (6 incorrect guesses allowed)")
    print("2. Medium (4 incorrect guesses allowed)")
    print("3. Hard   (2 incorrect guesses allowed)")

    while True:
        choice = input("Enter difficulty (1, 2, or 3): ")
        if choice == '1':
            return 6, "Easy"
        elif choice == '2':
            return 4, "Medium"
        elif choice == '3':
            return 2, "Hard"
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")

def play_hangman(tries_allowed, level_name):
    # Step 1: Predefined word list
    word_list = ["apple", "train", "house", "chair", "light"]

    # Step 2: Randomly choosing a word
    secret_word = random.choice(word_list)

    # Step 3: Initializing game state
    guessed_letters = []
    tries_left = tries_allowed
    word_display = ["_" for _ in secret_word]

    print(f"\n🔰 Difficulty Level: {level_name} — You have {tries_left} chances.")
    print("Guess the word one letter at a time.")

    # Step 4: Game loop
    while tries_left > 0 and "_" in word_display:
        print("\nWord: ", " ".join(word_display))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Tries left:", tries_left)

        guess = input("Enter a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct!")
            for idx, char in enumerate(secret_word):
                if char == guess:
                    word_display[idx] = guess
        else:
            print("❌ Incorrect!")
            tries_left -= 1

    # Step 5: End result
    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n💀 Game Over! The correct word was:", secret_word)

def main():
    while True:
        tries, level_name = get_difficulty()
        play_hangman(tries, level_name)

        # Ask to replay
        replay = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("👋 Thanks for playing Hangman! Goodbye.")
            break
        print("\n--- 🔄 Starting New Game ---\n")

# Starting the game
main()
