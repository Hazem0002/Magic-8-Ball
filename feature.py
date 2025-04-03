import random

responses = [
    "Yes, definitely.",
    "No, not now.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Outlook is good.",
    "Better not tell you now.",
    "Concentrate and ask again."
]

def get_random_response():
    return random.choice(responses)

def display_response(response):
    print("\n🔮 The Magic 8-Ball says:", response, "\n")

def play_again():
    while True:
        choice = input("Do you want to ask another question? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Please type 'yes' or 'no'.")

def get_user_question():
    question = input("Ask the Magic 8-Ball a yes/no question (or press Enter to quit): ").strip()
    return question if question else None

def magic_8_ball():
    print("🎱 Welcome to the Magic 8-Ball! 🎱")
    while True:
        question = get_user_question()
        if question is None:
            print("Goodbye!")
            break
        response = get_random_response()
        display_response(response)
        if not play_again():
            break

if __name__ == "__main__":
    magic_8_ball()
