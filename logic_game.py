import random

def generate_secret_number():
    """Generate a random three-digit number as a string with unique digits."""
    digits = random.sample(range(1, 10), 3)  # Ensure unique digits, no 0
    return "".join(map(str, digits))

def give_feedback(secret, guess):
    """Provide feedback on the guess compared to the secret number."""
    feedback = []
    
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("✔ Correct")
        elif guess[i] in secret:
            feedback.append("🔄 Misplaced")
        else:
            feedback.append("❌ Wrong")

    return feedback

def play_game():
    """Main function to run the deductive logic game."""
    secret_number = generate_secret_number()
    attempts = 0

    print("🔍 Welcome to the Deductive Logic Game!")
    print("Try to guess the secret three-digit number (digits are unique).")
    
    while True:
        guess = input("Enter your three-digit guess: ")
        
        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            print("❌ Invalid input! Enter a three-digit number with unique digits.")
            continue

        attempts += 1
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        
        feedback = give_feedback(secret_number, guess)
        print("Hint:", " | ".join(feedback))

if __name__ == "__main__":
    play_game()
