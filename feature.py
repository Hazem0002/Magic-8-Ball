
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
        choice = input("Do you want to ask another question? (yes/no):").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Please type 'yes' or 'no'.")

