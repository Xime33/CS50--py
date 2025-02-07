def main():
    saludo = input("Greeting: ").strip().title()
    saludar(saludo)


def saludar (greeting):
    if greeting.startswith("Hello"):
        print ("$0")
    elif greeting.startswith("H"):
        print ("$20")
    else:
        print ("$100")

main()
