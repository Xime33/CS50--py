import random


def main():
    level = get_level()
    score = diez(level)
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    while True:
        try:
            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
            elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
            else:
                x = random.randint(100,999)
                y = random.randint(100,999)

            return x, y


        except ValueError:
            pass

def diez(level):
    op = 1
    score= 0
    while op <= 10:
        x, y = generate_integer(level)
        respuesta = operaciones(x,y)
        if respuesta == True:
            score += 1
        op += 1
    return score


def operaciones (x,y):
    i = 1
    suma = x + y
    while i <= 3:
        try:
            respuesta = int(input(f"{x} + {y} = "))
            if suma == respuesta:
                return True
            else:
                i += 1
                print("EEE")
        except:
            i += 1
            print("EEE")
    print(f"{x} + {y} = {suma}")








if __name__ == "__main__":
    main()
