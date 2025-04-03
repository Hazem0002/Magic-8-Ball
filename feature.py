def play_again():
    while True:
        choice = input("Do you want to ask another question? (yes/no):
").strip().lower()
        if choice == "yes":
            return Trueelif choice == "no":
            print("Thanks for playing! Goodbye!")
            return Falseelse:
            print("Please type 'yes' or 'no'.")