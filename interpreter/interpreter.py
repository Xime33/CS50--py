def main():
    # ask the user for the input
    exp = input("Expression: ")
    print(f"{interpretador(exp):.1f}")


def interpretador(expresion):
    x, y, z = expresion.split()
    x = int(x)
    z = int(z)

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            return print("ERROR")


main()
