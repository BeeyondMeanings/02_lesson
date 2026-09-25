import random

WORDS = [
    "python",
    "computer",
    "programming",
    "puzzle",
    "keyboard",
    "science",
    "sunshine",
    "mountain",
    "challenge",
    "language",
    "desktop",
    "familiar",
    "joke",
    "suspense",
    "suffocate",
]


def scramble_word(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    return scrambled if scrambled != word else scramble_word(word)


def play_game() -> None:
    score = 0
    attempts = 0

    print("Welcome to the Word Puzzle Game!")
    print("Unscramble the letters to guess the word.\n")

    while True:
        word = random.choice(WORDS)
        scrambled = scramble_word(word)
        print(f"Puzzle: {scrambled}")

        guess = input("Enter your guess (or 'quit' to exit): ").strip().lower()

        if guess == "quit":
            print(f"\nGame over! Your final score is: {score}")
            break

        attempts += 1

        if guess == word:
            score += 1
            print("Correct!\n You got it right! 🎉")
            print(f"Your score is: {score}\n")
        else:
            print(f"Wrong! The correct answer is: {word}\n")


if __name__ == "__main__":

    
    play_game()
