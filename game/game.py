import random
import sys
# Prompts the user for a level n, If the user does not input a positive integer, the program should prompt again.


while True:
    try:
        usuario1 = int(input("Level: "))
        if usuario1 > 0:
            aleatorio = random.randint(1, usuario1)
            while True:
                try:
                    usuario2 = int(input("Guess: "))
                    if usuario2 < aleatorio:
                        print("Too small!")
                    elif usuario2 > aleatorio:
                        print("Too large!")
                    else:
                        if usuario2 == aleatorio:
                            print("Just right!")
                            sys.exit()
                except ValueError:
                    pass

        else:
            raise ValueError

    except ValueError:
        pass


# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
