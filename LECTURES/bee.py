WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to spelling Bee!!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper()
        if guess == "GRAPHIC":
            WORDS.clear()
            print("you have won!")
        if guess in WORDS.keys():
            points= WORDS.pop(guess)
            print(f"Great job! you scored {WORDS[points]} ponits.")


main()
